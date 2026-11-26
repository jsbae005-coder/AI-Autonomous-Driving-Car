"""A deterministic simulation for controller experiments.

This is an abstract lateral-error model, not a physical vehicle model. It is
useful for checking controller behaviour before hardware is available. Its
parameters must not be interpreted as measured vehicle characteristics.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PIDConfig:
    """PID gains and output limits."""

    kp: float
    ki: float
    kd: float
    output_limit: float = 1.0
    integral_limit: float = 2.0


class PIDController:
    """PID controller with bounded integral and output."""

    def __init__(self, config: PIDConfig) -> None:
        if config.output_limit <= 0:
            raise ValueError("output_limit must be positive")
        if config.integral_limit < 0:
            raise ValueError("integral_limit cannot be negative")
        self.config = config
        self._integral = 0.0
        self._previous_error: float | None = None

    def reset(self) -> None:
        """Clear accumulated controller state."""
        self._integral = 0.0
        self._previous_error = None

    def update(self, error: float, dt: float) -> float:
        """Return a bounded control command for the given error and time step."""
        if dt <= 0:
            raise ValueError("dt must be positive")
        self._integral += error * dt
        limit = self.config.integral_limit
        self._integral = max(-limit, min(limit, self._integral))
        derivative = 0.0
        if self._previous_error is not None:
            derivative = (error - self._previous_error) / dt
        self._previous_error = error
        output = (self.config.kp * error + self.config.ki * self._integral + self.config.kd * derivative)
        bound = self.config.output_limit
        return max(-bound, min(bound, output))


@dataclass
class SimulatedVehicle:
    """Abstract vehicle whose lateral error responds to steering input.

    Positive steering reduces positive lateral error. Parameters are
    dimensionless simulation assumptions, not hardware measurements.
    """

    lateral_error: float = 0.6
    correction_gain: float = 0.25
    disturbance: float = 0.0

    def step(self, steering: float) -> float:
        if not -1.0 <= steering <= 1.0:
            raise ValueError("steering must be in [-1.0, 1.0]")
        self.lateral_error += self.disturbance - self.correction_gain * steering
        return self.lateral_error


def run_simulation(*, steps: int = 100, dt: float = 0.05,
                   initial_error: float = 0.6,
                   config: PIDConfig = PIDConfig(kp=1.2, ki=0.0, kd=0.08),
                   correction_gain: float = 0.25,
                   disturbance: float = 0.0) -> list[float]:
    """Run an abstract closed-loop test and return lateral error per step."""
    if steps <= 0:
        raise ValueError("steps must be positive")
    controller = PIDController(config)
    vehicle = SimulatedVehicle(initial_error, correction_gain, disturbance)
    errors = [vehicle.lateral_error]
    for _ in range(steps):
        steering = controller.update(vehicle.lateral_error, dt)
        errors.append(vehicle.step(steering))
    return errors
