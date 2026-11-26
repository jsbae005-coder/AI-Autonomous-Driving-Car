# Historical Hardware Configuration and Reproduction Notes

## Confirmed project configuration

- Robotics platform: UBION DeepCobot experimental kit
- Visual input: Raspberry Pi camera
- Demonstration outcome: autonomous driving on the prepared course was completed
- Final implementation did not use HuskyLens or an ultrasonic sensor

## Reproduction boundary

The original source code, exact wiring record, camera settings, and dated measurement logs are not available in this repository. For that reason, this page does not invent GPIO assignments, motor-driver pins, baud rates, camera resolution, or performance figures.

The Python control module is a hardware-independent reconstruction. It is not ready to be connected directly to motors without a verified hardware adapter.

## Before reproducing on hardware

1. Identify the exact DeepCobot controller and motor-driver board revision.
2. Confirm the camera model, interface, resolution, and frame rate.
3. Verify motor wiring, voltage/current ratings, and power arrangement.
4. Keep wheels lifted during initial actuator checks.
5. Verify an emergency-stop mechanism before autonomous motion.
6. Start at low speed in a clear, controlled test area.
7. Record dated video and repeatable measurements before publishing numerical performance claims.

Never infer pin assignments or electrical limits from a generic example.
