# Project Report

## Project

**Experimental-kit AI autonomous vehicle driving-stability improvement project**

- Team: STM (Science Technology Makers)
- Platform: UBION DeepCobot
- Visual sensor: Raspberry Pi camera
- Main objective: complete autonomous path following and improve driving stability on the prepared course

## Background

A small autonomous vehicle must repeatedly interpret its surroundings and correct its direction while moving. Small errors in visual path detection or steering can accumulate, especially around bends. This project focused on using camera-based visual input to follow a prepared driving path and adjusting control behaviour for more stable movement.

## Implementation

The team assembled and studied the DeepCobot platform, connected the Raspberry Pi camera, and developed the driving flow around visual path information. The vehicle used the camera view to determine path position and adjusted its movement to remain on the course.

The final project demonstration achieved autonomous driving on the prepared course. The work involved integration of the experimental platform, camera-based perception, steering behaviour, and repeated driving adjustments.

## Result

- Completed autonomous driving demonstration on the prepared course.
- Used Raspberry Pi camera input for visual path tracking.
- Integrated path perception with vehicle steering behaviour.
- Focused on improving driving stability through iterative testing and adjustment.

No numerical accuracy, speed, completion-rate, or lap-time result is included because a verified measurement record is not available in the current repository.

## Repository reconstruction note

The original project source code and raw hardware records were not retained. The Python modules now published here are a clean reconstruction intended to make the core perception-to-control logic understandable, testable, and maintainable. They are not a recovered copy of the original firmware.

## Learning outcomes

- Embedded robotics system integration
- Camera-based visual perception
- Closed-loop control concepts
- Debugging and iterative hardware testing
- Separating hardware-specific I/O from reusable control logic
