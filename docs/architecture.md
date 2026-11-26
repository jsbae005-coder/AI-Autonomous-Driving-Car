# Software Architecture

## Current development stage

This repository is being rebuilt as a simulation-first project. Historical
source code and hardware photographs are unavailable. The original project
description reports use of HuskyLens for line tracking and basic forward,
turn, and stop behaviour, but the exact Arduino model, motor driver, wiring,
and communication settings have not been recovered.

## Proposed layers

1. **Perception** — receive and validate line observations from HuskyLens.
2. **State estimation** — calculate normalized lateral tracking error and
detect missing or stale observations.
3. **Control** — compute bounded steering correction; PID is the initial
candidate controller.
4. **Actuation** — translate steering and speed requests into motor-driver
commands for the verified board and driver.
5. **Safety** — stop motors on stale sensor data, invalid commands, startup,
or emergency-stop activation.
6. **Telemetry** — record sensor status, error, controller output, and safety
state for repeatable evaluation.

## Current implementation

- simulation/line_following.py: abstract lateral-error model and bounded PID.
- tests/test_line_following.py: initial unit tests for controller limits and
  simulation behaviour.

## Hardware boundary

No Arduino firmware is claimed to be hardware-ready yet. Before firmware is
written, confirm the exact board, motor driver, motor wiring, HuskyLens
protocol (UART or I2C), baud rate/address, and power arrangement. Pin numbers
and motor polarity must never be guessed.

## Engineering principles

- Keep hardware I/O separate from control logic.
- Validate sensor data before using it.
- Bound all actuator commands.
- Prefer a safe stop over continuing with invalid or stale perception.
- Record assumptions and distinguish simulated results from measured results.
