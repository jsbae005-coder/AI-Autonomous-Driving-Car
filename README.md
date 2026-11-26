# AI Autonomous Driving Car

**Simulation-first rebuild of a HuskyLens-based line-following robotics project.**

This repository separates the historical project description from newly developed and testable software. The original EIE-Makers project was described as an Arduino-based vehicle using HuskyLens for line tracking, with forward, turn, stop, and direction-correction behaviour. Its original source code and hardware records are no longer available.

The current repository is therefore a **rebuild in progress**, not a claim that the original firmware has been recovered or that new algorithms have already been validated on a physical car.

## Project goals

- Build a modular line-following control system.
- Explore bounded PID control and recovery behaviour.
- Validate software logic in a deterministic simulator before hardware tests.
- Add Arduino firmware only after the exact board, motor driver, wiring, and HuskyLens communication settings are confirmed.
- Publish reproducible tests and measured results.

## Repository structure

| Path | Purpose |
|---|---|
| `simulation/` | Hardware-independent control experiments |
| `tests/` | Automated software tests |
| `docs/architecture.md` | System boundaries and design decisions |
| `docs/hardware-validation.md` | Hardware identification and safe bring-up checklist |
| `firmware/` | Reserved for board-specific embedded firmware |

## Current status

- [x] Repository created
- [x] Initial project documentation
- [x] Simulation-first architecture documented
- [x] Initial bounded PID and abstract vehicle model
- [x] Initial automated tests
- [ ] Confirm exact Arduino board and motor driver
- [ ] Verify HuskyLens UART/I2C configuration
- [ ] Implement board-specific firmware
- [ ] Run hardware tests and publish measured results

## Run the tests

Python 3.10 or newer is required.

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

The simulation is an abstract software model. Its parameters are illustrative, not measured physical vehicle constants. Passing simulation tests does not prove real-world driving performance.

## Safety

Do not connect motors using guessed pin assignments. Confirm board, motor driver, wiring, voltage, and current limits first. Test motor outputs with wheels lifted and verify an emergency stop before any autonomous run.

## Project documentation

- [Software architecture](docs/architecture.md)
- [Hardware validation checklist](docs/hardware-validation.md)

**Build. Test. Measure. Improve.**
