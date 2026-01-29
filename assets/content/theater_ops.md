### 1. Power-Up Sequence
**CRITICAL:** Do not turn on the amps until the mixing console has fully booted.

1.  Toggle the main breaker (Left Rack).
2.  Wait for the `Midas M32` logo to appear on the console.
3.  Turn on the L/R Speakers (Green Switch).

### 2. Digital Patching
If the wireless mics are not routing, check the input block:

| Channel | Input Source | Phantom Power |
| :--- | :--- | :--- |
| 1-8 | Stage Box A | OFF |
| 9-12 | Wireless Rack | OFF |
| 16 | Overhead Mic | **ON (+48v)** |

### 3. Emergency Reset
If the system freezes, run the soft-reset command on the macro pad or execute:

```bash
# System Panic Script
sudo systemctl restart audio_engine