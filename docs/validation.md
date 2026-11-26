# Software Validation

## Scope

These checks validate the reconstructed Python components. They do not reproduce the historical physical vehicle demonstration and do not establish measured driving performance.

## Automated checks

Run:

    python -m pip install -e ".[dev]"
    python -m pytest -q

The test suite covers:

- Path centroid extraction from a binary image mask
- Normalized error direction
- Empty and malformed input handling
- Safe stop when the path is lost
- Reduced speed for low-confidence perception
- Bounded steering output
- PID output limits and reset behaviour
- Expected convergence direction in the abstract simulation

## Interpretation

A passing test suite means the reconstructed software contracts behave as specified under the test cases. It does not mean the code has been flashed to DeepCobot or validated on a physical course. Physical claims belong in a separate test log with dated video, configuration, and repeatable measurements.
