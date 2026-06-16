# MYTHOS ENTERPRISE DEPLOYMENT MAKEFILE

.PHONY: help install run clean

help:
	@echo "Mythos Core Deployment Commands:"
	@echo "  make install  - Initializes the cognitive core and compiles vectors."
	@echo "  make run      - Launches the interactive terminal workspace."
	@echo "  make clean    - Wipes local memory states (Reset)."

install:
	@chmod +x bin/init_mythos.sh
	@./bin/init_mythos.sh

run:
	@python3 bin/launch_mythos.py

clean:
	@rm -f .mythos_history.json
	@echo "[!] Memory cache wiped cleanly."
