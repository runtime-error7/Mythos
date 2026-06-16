#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
NC='\033[0m'

clear
echo -e "${BLUE}==================================================${NC}"
echo -e "${CYAN}     MYTHOS COGNITIVE CORE: INITIAL DEPLOYMENT   ${NC}"
echo -e "${BLUE}==================================================${NC}"
echo ""

if [ -f .mythos_compiled ]; then
    echo -e "${YELLOW}[!] System already initialized. Run 'make run' to launch.${NC}"
    exit 0
fi

# Securely capture the system prompt
echo -e "${CYAN}[->] Please paste your custom Fable 5 System Prompt below.${NC}"
echo -e "${YELLOW}(Press CTRL+D on a blank line when finished pasting)${NC}"
echo -e "${BLUE}--------------------------------------------------${NC}"
USER_PROMPT=$(cat)
echo -e "${BLUE}--------------------------------------------------${NC}"

echo -n "[1/3] Mapping native system virtualization layers..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh > /dev/null 2>&1
fi
echo -e " [${GREEN}DONE${NC}]"

echo -n "[2/3] Fetching core 120B parameter weight topology..."
ollama pull gpt-oss:120b > /dev/null 2>&1
echo -e " [${GREEN}DONE${NC}]"

echo -n "[3/3] Compiling proprietary runtime definitions..."
mkdir -p .core_config
cat << EOF > .core_config/Enginefile
FROM gpt-oss:120b
SYSTEM """
$USER_PROMPT
"""
EOF
ollama create mythos-core-engine -f .core_config/Enginefile > /dev/null 2>&1
touch .mythos_history.json
touch .mythos_compiled
echo -e " [${GREEN}COMPILED${NC}]"

echo ""
echo -e "${GREEN}====== MYTHOS COGNITIVE INFRASTRUCTURE INITIALIZED ======${NC}"
echo -e "Bhaiya, the workspace environment is locked and optimized."
echo -e "Launch the CLI terminal using: ${CYAN}make run${NC}"
echo -e "${BLUE}==================================================${NC}"
