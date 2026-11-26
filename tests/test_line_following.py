import pytest

from simulation.line_following import PIDConfig, PIDController, run_simulation


def test_pid_output_is_bounded() -> None:
    controller = PIDController(PIDConfig(kp=10.0, ki=2.0, kd=1.0, output_limit=0.7))
    assert controller.update(100.0, 0.1) == pytest.approx(0.7)
    assert controller.update(-100.0, 0.1) == pytest.approx(-0.7)


def test_pid_rejects_non_positive_dt() -> None:
    controller = PIDController(PIDConfig(kp=1.0, ki=0.0, kd=0.0))
    with pytest.raises(ValueError):
        controller.update(0.2, 0.0)


def test_pid_reset_clears_previous_state() -> None:
    controller = PIDController(PIDConfig(kp=0.0, ki=0.0, kd=1.0))
    controller.update(1.0, 0.1)
    controller.reset()
    assert controller.update(0.5, 0.1) == pytest.approx(0.0)


def test_simulation_moves_error_toward_zero_without_disturbance() -> None:
    errors = run_simulation(steps=30, initial_error=0.6)
    assert abs(errors[-1]) < abs(errors[0])


def test_simulation_rejects_invalid_step_count() -> None:
    with pytest.raises(ValueError):
        run_simulation(steps=0)
