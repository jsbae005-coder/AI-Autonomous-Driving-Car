# System Architecture

## 1. Overview

The historical build used a UBION DeepCobot experimental robotics platform and a Raspberry Pi camera. Camera frames provided the visual input for path-following and autonomous driving on the prepared course.

This document describes the functional system. The Python package in this repository is a hardware-independent reconstruction of the perception-to-control boundary; it is not the original camera capture stack or motor firmware.

## 2. Data flow

1. Image acquisition: Raspberry Pi camera provides a frame.
2. Path perception: image processing isolates the path region and produces a binary mask.
3. Position estimation: the lower image region estimates the horizontal path centroid.
4. Error calculation: centroid position is normalized relative to image center.
5. Steering control: bounded PID control converts lateral error into a steering correction.
6. Vehicle actuation: the platform drive system applies the requested motion.
7. Feedback: the next camera frame closes the loop.

## 3. Reconstructed software modules

| Module | Responsibility |
|---|---|
| control.line_follower | Path-mask centroid, confidence, bounded steering command, fail-safe state |
| simulation.line_following | Abstract vehicle model and PID controller |
| tests | Deterministic unit tests for perception and control behaviour |

## 4. Control and safety decisions

- Normalize path position to [-1, 1] so control logic is independent of image width.
- Use the lower image region to prioritize the path nearest the vehicle.
- Bound steering output to prevent unbounded control requests.
- Reduce commanded speed when perception confidence is weak.
- Return a zero-speed command when the path is missing or confidence is below threshold.
- Reset accumulated PID state after line loss to avoid stale controller state.

## 5. Hardware integration boundary

The repository does not assume undocumented GPIO pins, motor-driver wiring, PWM frequencies, or camera settings. These must be taken from the actual DeepCobot kit documentation and verified hardware configuration before connecting the reconstructed controller to a physical platform.

## 6. Limitations

The path mask is an input contract. Camera calibration, image segmentation, perspective correction, and frame acquisition are not represented as recovered historical code. The abstract simulator is useful for deterministic software experiments but is not a calibrated vehicle dynamics model.
