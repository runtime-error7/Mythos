# Enterprise Troubleshooting Guide

If you experience anomalies during your session, consult the matrices below before submitting an issue to the engineering team.

### Issue 1: "Connection Interrupted. Infrastructure node offline."
**Symptom:** You type a command in the CLI, but it immediately fails with a network exception.
**Diagnosis:** The background engine failed to bind to Local Socket `11434`.
**Resolution:** 1. Ensure no other applications are using port `11434`.
2. Terminate the application via `/exit`.
3. Restart the background virtualization node and try launching again.

### Issue 2: Extreme Latency / "Thinking" Animation Hangs
**Symptom:** The `mythos-engine thinking` loader spins for more than 45 seconds without an output stream.
**Diagnosis:** Your system is aggressively offloading generation layers from VRAM to standard system RAM due to memory limitations.
**Resolution:** Close high-memory background applications (e.g., Chrome, Docker containers not related to the project) and execute `/clear` to free visual buffer space.

### Issue 3: "Run 'make install' once to compile core vectors"
**Symptom:** The CLI refuses to launch and outputs a yellow warning flag.
**Diagnosis:** You bypassed the initialization script or the `.mythos_compiled` lock file was deleted.
**Resolution:** Run `make install` from your standard terminal to rebuild the system parameters.

### Wiping Contaminated Memory
If the agent begins repeating past mistakes or applying the wrong context to a new project task, the contextual memory tracks may be saturated. 
**Resolution:** Type `/reset` in the interactive console, or run `make clean` from standard bash. This flushes the JSON array entirely while keeping the underlying Fable 5 engine rules intact.
