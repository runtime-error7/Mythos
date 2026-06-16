# ⚡ MYTHOS ENTERPRISE
**High-Capacity Cognitive Operator Framework (v3.0.0-Stable)**
![Version](https://img.shields.io/badge/Version-3.0.0--Enterprise-blue)
![Architecture](https://img.shields.io/badge/Architecture-120B_MoE-orange)
![State](https://img.shields.io/badge/State-Persistent_Memory-success)
![License](https://img.shields.io/badge/License-Proprietary-red)
Welcome to the **Mythos Enterprise Distribution**. This repository contains the secure deployment binaries for a fully localized 120B parameter cognitive agent. Driven by strict Fable 5 deterministic logic constraints, this system is engineered for autonomous terminal operations, deep context retention, and absolute zero-leak data privacy.
---
## 🚀 Key Capabilities
*   **Air-Gapped Privacy:** All generational processing happens natively on your host machine. Zero external API calls, zero telemetry tracking.
*   **Persistent Context Mapping:** Custom JSON-array memory architectures allow the operator to retain cross-session task awareness indefinitely.
*   **Asynchronous Headless Execution:** Terminal outputs and processes run in non-blocking background threads, ensuring a clean, distraction-free workspace.
*   **Fable 5 Guardrails:** The inference engine is hard-locked to highly rigid behavioral bounds, preventing system-level logic hallucinations.
---
## 🏗️ System Requirements
Ensure your bare-metal or hypervisor environment meets the following specifications before initiating the build matrix:

| Component | Minimum Specification | Recommended (High-Throughput) |
| :--- | :--- | :--- |
| **Storage** | 65 GB SSD | 100+ GB NVMe Storage |
| **Memory (RAM/VRAM)** | 64GB System RAM (Layer Offload) | 80GB Enterprise VRAM (H100/A100) |
| **OS Environment** | Ubuntu 22.04 LTS / Debian 12 | Ubuntu 22.04 LTS |
| **Dependencies** | `python3`, `curl`, `make` | Sandboxed Docker/WSL2 Node |

---
## ⚙️ Deployment Protocol
We utilize standard GNU Make protocols to handle virtualization setup. Background weights, dependencies, and configuration layers will be securely fetched and compiled locally.
### Step 1: Initial Core Compilation
Run the deployment sequence to download the foundational neural matrices and inject your authorized configuration payload.
```bash
make install
```
*> 🔒 Security Note: You will be prompted to inject your authorized System Prompt token during this phase. Ensure you have it copied to your clipboard.*
### Step 2: Initialize Agentic Workspace
Once the compilation lock (`.mythos_compiled`) is generated, spin up the active tracking environment and establish the network socket:
```bash
make run
```
---
## 🎛️ Command Glossary
While inside the interactive Mythos Terminal CLI, use these slash commands to manipulate the active engine state:
*   `/clear`   — Purge visual terminal artifacts and refresh the UI.
*   `/history` — Output the active context tracks from the memory array.
*   `/reset`   — Safely destroy active session memory. Use this when pivoting to a completely new project to prevent context contamination.
*   `/exit`    — Disconnect the network socket and write memory layers to disk securely.
*(Note: Memory can also be wiped externally by executing `make clean` in your standard bash terminal).*
---
## 🛡️ Support & Troubleshooting
If you encounter runtime latency or connection matrix errors:
1. Verify no other processes are occupying port `11434`.
2. Check your hardware resource allocation.
3. Submit a detailed ticket via the repository's **Issues** tab using the provided Enterprise Template.
---
## ⚖️ Licensing & Compliance
This software distribution is strictly **Proprietary and Confidential**. Unauthorized modification, redistribution, or reverse engineering of the background execution engine is an explicit violation of the software license. Contact your designated integration engineer for pipeline updates or node scaling.
