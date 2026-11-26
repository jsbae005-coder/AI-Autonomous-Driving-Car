"""Reconstructed camera-mask perception and steering-control pipeline.

This hardware-independent module accepts a binary path mask produced by an
image-processing stage and returns a bounded steering command. It is not the
original DeepCobot firmware and does not access a Raspberry Pi camera.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Sequence

from simulation.line_following import PIDConfig, PIDController


class TrackingState(str, Enum):
    TRACKING = "tracking"
    LOW_CONFIDENCE = "low_confidence"
    LINE_LOST = "line_lost"


@dataclass(frozen=True)
class PathObservation:
    """Normalized path location and quality derived from a binary image mask."""

    center_error: float
    confidence: float
    pixel_count: int


@dataclass(frozen=True)
class SteeringCommand:
    """Safe, bounded output from one control update."""

    steering: float
    speed_scale: float
    state: TrackingState
    center_error: float
    confidence: float


def extract_path_observation(
    mask: Sequence[Sequence[bool]],
    *,
    min_pixels: int = 3,
    roi_start: float = 0.5,
) -> PathObservation | None:
    """Find the horizontal center of a path mask in the lower image region.

    True pixels represent the detected path. The lower region is used because
    it is closest to the vehicle. Error is normalized to [-1, 1], where zero
    means the path is centered in the image.
    """
    if not mask or not mask[0]:
        raise ValueError("mask must be a non-empty rectangular matrix")
    if not 0.0 <= roi_start < 1.0:
        raise ValueError("roi_start must be in [0, 1)")
    if min_pixels < 1:
        raise ValueError("min_pixels must be at least 1")

    width = len(mask[0])
    if any(len(row) != width for row in mask):
        raise ValueError("mask rows must have equal width")

    start_row = min(int(len(mask) * roi_start), len(mask) - 1)
    xs = [
        x
        for row in mask[start_row:]
        for x, is_path in enumerate(row)
        if is_path
    ]
    if len(xs) < min_pixels:
        return None

    centroid = sum(xs) / len(xs)
    center = (width - 1) / 2
    scale = max(center, 1.0)
    error = max(-1.0, min(1.0, (centroid - center) / scale))
    roi_area = (len(mask) - start_row) * width
    confidence = min(1.0, len(xs) / max(roi_area * 0.08, 1.0))
    return PathObservation(error, confidence, len(xs))


class CameraLineFollower:
    """Convert camera-derived path observations into bounded steering commands."""

    def __init__(
        self,
        pid: PIDConfig = PIDConfig(kp=0.75, ki=0.02, kd=0.08, output_limit=1.0),
        *,
        min_confidence: float = 0.05,
        reduced_speed_confidence: float = 0.2,
    ) -> None:
        if not 0.0 <= min_confidence <= 1.0:
            raise ValueError("min_confidence must be in [0, 1]")
        if not min_confidence <= reduced_speed_confidence <= 1.0:
            raise ValueError("reduced_speed_confidence must be between min_confidence and 1")
        self.controller = PIDController(pid)
        self.min_confidence = min_confidence
        self.reduced_speed_confidence = reduced_speed_confidence

    def update(self, observation: PathObservation | None, dt: float) -> SteeringCommand:
        """Return steering and speed scaling; weak perception fails safe."""
        if dt <= 0:
            raise ValueError("dt must be positive")
        if observation is None or observation.confidence < self.min_confidence:
            self.controller.reset()
            return SteeringCommand(0.0, 0.0, TrackingState.LINE_LOST, 0.0, 0.0)

        if not -1.0 <= observation.center_error <= 1.0:
            raise ValueError("center_error must be normalized to [-1, 1]")
        if not 0.0 <= observation.confidence <= 1.0:
            raise ValueError("confidence must be in [0, 1]")

        steering = self.controller.update(observation.center_error, dt)
        if observation.confidence < self.reduced_speed_confidence:
            return SteeringCommand(
                steering, 0.35, TrackingState.LOW_CONFIDENCE,
                observation.center_error, observation.confidence,
            )
        return SteeringCommand(
            steering, 1.0, TrackingState.TRACKING,
            observation.center_error, observation.confidence,
        )
