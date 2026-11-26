# DeepCobot Camera-Based Autonomous Line-Following Robot

**EIE-Makers Project · STM (Science Technology Makers)**  
Robotics · Embedded Systems · Computer Vision · Control

A robotics project focused on improving the driving stability of an experimental-kit autonomous vehicle. The team used a UBION DeepCobot platform and Raspberry Pi camera to perceive the driving path, calculate steering corrections, and complete autonomous driving on the prepared course.

The original project source files are no longer available. This repository therefore contains a documented software reconstruction and a reproducible, hardware-independent control test suite. The Python modules are not represented as the original DeepCobot firmware.

## Project at a glance

| Item | Description |
|---|---|
| Project | Experimental-kit AI autonomous vehicle driving-stability improvement |
| Platform | UBION DeepCobot |
| Visual sensor | Raspberry Pi camera |
| Core task | Camera-based path tracking and autonomous driving |
| Control focus | Steering correction and stable path following |
| Team | STM (Science Technology Makers) |
| Domain | Robotics, embedded systems, computer vision, control |

## Key outcomes

- Completed autonomous driving demonstration on the prepared course.
- Used Raspberry Pi camera input for visual path tracking.
- Integrated visual path position with steering behaviour.
- Iteratively adjusted driving behaviour to improve stability.

**Hardware clarification:** The final implementation used a Raspberry Pi camera. HuskyLens and ultrasonic sensing were not used in the final build.

## Repository structure

    .
    ├── control/
    │   └── line_follower.py       # Reconstructed path-mask to steering pipeline
    ├── simulation/
    │   └── line_following.py      # Abstract closed-loop PID simulation
    ├── tests/
    │   ├── test_line_follower.py  # Perception/control unit tests
    │   └── test_line_following.py # PID and simulation tests
    ├── docs/
    │   ├── architecture.md
    │   ├── project-report.md
    │   └── validation.md
    └── .github/workflows/
        └── python-tests.yml

## Run locally

Python 3.10 or newer.

    python -m pip install -e ".[dev]"
    python -m pytest

## System flow

    Raspberry Pi Camera
            |
            v
      Image / Path Region
            |
            v
       Path Position
            |
            v
       Lateral Error
            |
            v
     Steering Controller
            |
            v
       DeepCobot Drive
            |
            v
       Vehicle Motion
            |
            +------ feedback to camera

## Evidence and engineering transparency

This repository separates three kinds of evidence:

1. Historical project outcome: the team completed autonomous driving on its prepared course.
2. Reconstructed software: the Python modules are a clean, testable reconstruction because the original source was not retained.
3. Current automated validation: tests cover path-position extraction, confidence handling, steering bounds, fail-safe behaviour, and an abstract PID simulation.

The automated tests do not replace physical vehicle measurements. No unverified speed, accuracy, lap-time, or success-rate figures are reported.

## Documentation

- [Architecture and data flow](docs/architecture.md)
- [Project report](docs/project-report.md)
- [Validation and test coverage](docs/validation.md)

**Build · Observe · Correct · Validate**
