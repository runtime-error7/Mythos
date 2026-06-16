#!/usr/bin/env python3
import os
import sys
import json
import time
import urllib.request
import urllib.error
try:
    import readline  # Enables terminal arrow-key command history navigation
except ImportError:
    pass

# System Styling Matrix (Claude Code Aesthetic)
BG_DARK = "\033[40m"
TEXT_WHITE = "\033[97m"
TEXT_GREEN = "\033[32m"
TEXT_CYAN = "\033[36m"
TEXT_YELLOW = "\033[33m"
TEXT_GRAY = "\033[90m"
STYLE_BOLD = "\033[1m"
RESET = "\033[0m"

class MythosCLI:
    def __init__(self):
        self.history_file = ".mythos_history.json"
        self.api_url = "http://localhost:11434/api/chat"
        self.model_name = "mythos-core-engine"
        
        if not os.path.exists(".mythos_compiled"):
            print(f"{TEXT_YELLOW}[!] Run 'make install' once to compile core vectors first.{RESET}")
            sys.exit(1)
            
        self.memory = self.load_memory_context()

    def print_banner(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        banner = f"""{TEXT_CYAN}{STYLE_BOLD}
███╗   ███╗██╗   ██╗████████╗██╗  ██╗ ██████╗ ███████╗
████╗ ████║╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗██╔════╝
██╔████╔██║ ╚████╔╝    ██║   ███████║██║   ██║███████╗
██║╚██╔╝██║  ╚██╔╝     ██║   ██╔══██║██║   ██║╚════██║
██║ ╚═╝ ██║   ██║      ██║   ██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝{RESET}
 {TEXT_GRAY}v3.0.0-Stable // Local Asynchronous Agent Engine // Memory State: Connected{RESET}
 {TEXT_GRAY}Type {TEXT_YELLOW}/clear{TEXT_GRAY} to flush screen, {TEXT_YELLOW}/reset{TEXT_GRAY} to wipe memory, {TEXT_YELLOW}/exit{TEXT_GRAY} to disconnect.{RESET}
{TEXT_CYAN}---------------------------------------------------------------------{RESET}"""
        print(banner)

    def load_memory_context(self):
        if os.path.exists(self.history_file) and os.path.getsize(self.history_file) > 0:
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_memory_context(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def show_loading_indicator(self, stop_event):
        # Subtle, professional terminal processing animation
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        i = 0
        sys.stdout.write(f"\n{TEXT_GRAY}┠─ mythos-engine thinking ")
        while not stop_event[0]:
            sys.stdout.write(chars[i])
            sys.stdout.flush()
            sys.stdout.write("\b")
            i = (i + 1) % len(chars)
            time.sleep(0.08)
        # Clear loading line text cleanly
        sys.stdout.write("\r" + " " * 40 + "\r")
        sys.stdout.flush()

    def dispatch_network_request(self, prompt):
        # Maps chat roles and builds standard array payloads directly to the background service port
        formatted_messages = []
        for turn in self.memory:
            formatted_messages.append({"role": turn["role"], "content": turn["content"]})
        
        formatted_messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": self.model_name,
            "messages": formatted_messages,
            "stream": False
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.api_url, 
            data=data, 
            headers={"Content-Type": "application/json"}
        )
        
        # Launch non-blocking animation handle
        stop_signal = [False]
        import threading
        loader_thread = threading.Thread(target=self.show_loading_indicator, args=(stop_signal,))
        loader_thread.start()
        
        try:
            with urllib.request.urlopen(req) as response:
                res_body = json.loads(response.read().decode("utf-8"))
                output_text = res_body["message"]["content"]
                status = "success"
        except urllib.error.URLError as e:
            output_text = f"Connection Interrupted. Infrastructure node offline. Info: {str(e)}"
            status = "error"
        except Exception as e:
            output_text = f"Internal Exception encountered during runtime parse. Info: {str(e)}"
            status = "error"
            
        stop_signal[0] = True
        loader_thread.join()
        return status, output_text

    def start_loop(self):
        self.print_banner()
        
        # Display existing historical data on boot if it exists
        if self.memory:
            print(f"{TEXT_GRAY}>>> Loaded continuous session history ({len(self.memory) // 2} previous turns).{RESET}\n")
        
        while True:
            try:
                # Custom interactive console cursor string matching Claude Code CLI layout
                user_input = input(f"{STYLE_BOLD}{TEXT_GREEN}mythos-user {TEXT_WHITE}› {RESET}").strip()
                
                if not user_input:
                    continue
                
                # Command Router Interventions
                if user_input.lower() == '/exit' or user_input.lower() == '/quit':
                    print(f"\n{TEXT_GRAY}Stopping Mythos Operator session safely. Context preserved.{RESET}")
                    break
                elif user_input.lower() == '/clear':
                    self.print_banner()
                    continue
                elif user_input.lower() == '/reset':
                    self.memory = []
                    self.save_memory_context()
                    print(f"\n{TEXT_YELLOW}[!] Long-term memory context cache wiped successfully.{RESET}\n")
                    continue
                elif user_input.lower() == '/history':
                    print(f"\n{TEXT_CYAN}=== ACTIVE RUNTIME MEMORY ENTRIES ==={RESET}")
                    for entry in self.memory:
                        role_label = "User" if entry['role'] == 'user' else "Agent"
                        print(f"{STYLE_BOLD}[{role_label}]{RESET}: {entry['content'][:100]}...")
                    print(f"{TEXT_CYAN}====================================={RESET}\n")
                    continue
                elif user_input.startswith('/'):
                    print(f"{TEXT_YELLOW}Unknown system command. Available parameters: /clear, /history, /reset, /exit{RESET}\n")
                    continue

                # Process payload transmission
                status, execution_response = self.dispatch_network_request(user_input)
                
                # Standard Output Printing
                print(f"\n{STYLE_BOLD}{TEXT_CYAN}mythos-agent{RESET}")
                print(f" {execution_response.strip()}")
                print(f"\n{TEXT_GRAY}─────────────────────────────────────────────────────────────────────{RESET}\n")
                
                if status == "success":
                    self.memory.append({"role": "user", "content": user_input})
                    self.memory.append({"role": "assistant", "content": execution_response})
                    self.save_memory_context()
                    
            except (KeyboardInterrupt, EOFError):
                print(f"\n\n{TEXT_GRAY}Session terminated via terminal interrupt signaling. Exiting.{RESET}")
                break

if __name__ == "__main__":
    client = MythosCLI()
    client.start_loop()
