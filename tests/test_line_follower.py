import pytest

from control.line_follower import (
    CameraLineFollower,
    PathObservation,
    TrackingState,
    extract_path_observation,
)


def test_centered_path_has_zero_error():
    mask = [[False] * 9 for _ in range(6)]
    for row in mask[3:]:
        row[4] = True
    observation = extract_path_observation(mask, min_pixels=2)
    assert observation is not None
    assert observation.center_error == pytest.approx(0.0)


def test_right_of_center_path_has_positive_error():
    mask = [[False] * 9 for _ in range(6)]
    for row in mask[3:]:
        row[6] = True
    observation = extract_path_observation(mask, min_pixels=2)
    assert observation is not None
    assert observation.center_error > 0


def test_left_of_center_path_has_negative_error():
    mask = [[False] * 9 for _ in range(6)]
    for row in mask[3:]:
        row[2] = True
    observation = extract_path_observation(mask, min_pixels=2)
    assert observation is not None
    assert observation.center_error < 0


def test_missing_path_returns_none():
    assert extract_path_observation([[False] * 8 for _ in range(8)]) is None


def test_invalid_ragged_mask_is_rejected():
    with pytest.raises(ValueError):
        extract_path_observation([[False, True], [False]])


def test_line_loss_commands_safe_stop():
    command = CameraLineFollower().update(None, 0.05)
    assert command.state is TrackingState.LINE_LOST
    assert command.speed_scale == 0.0
    assert command.steering == 0.0


def test_low_confidence_reduces_speed():
    follower = CameraLineFollower(reduced_speed_confidence=0.5)
    command = follower.update(PathObservation(0.3, 0.1, 5), 0.05)
    assert command.state is TrackingState.LOW_CONFIDENCE
    assert command.speed_scale == 0.35


def test_steering_is_bounded():
    command = CameraLineFollower().update(PathObservation(1.0, 0.9, 30), 0.05)
    assert -1.0 <= command.steering <= 1.0


def test_invalid_dt_is_rejected():
    with pytest.raises(ValueError):
        CameraLineFollower().update(PathObservation(0.0, 0.9, 10), 0.0)
