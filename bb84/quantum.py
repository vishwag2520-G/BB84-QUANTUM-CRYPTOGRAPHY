import numpy as np

# Computational basis states
ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)

# Diagonal basis states
PLUS = np.array([1, 1], dtype=complex) / np.sqrt(2)
MINUS = np.array([1, -1], dtype=complex) / np.sqrt(2)

# Hadamard gate
H = np.array([
    [1, 1],
    [1, -1]
], dtype=complex) / np.sqrt(2)


def encode_qubit(bit, basis):
    """Encode a classical bit into a BB84 quantum state."""

    if bit not in (0, 1):
        raise ValueError("Bit must be 0 or 1")

    if basis == "Z":
        return ZERO.copy() if bit == 0 else ONE.copy()

    elif basis == "X":
        return PLUS.copy() if bit == 0 else MINUS.copy()

    else:
        raise ValueError("Basis must be Z or X")


def measure_qubit(state, basis, rng=None):
    """Measure a normalized qubit state in the Z or X basis."""

    state = np.asarray(state, dtype=complex)
    if not np.all(np.isfinite(state)):
        raise ValueError("State must contain finite values")

    if state.shape != (2,):
        raise ValueError("State must be a two-element vector")

    norm = np.linalg.norm(state)

    if not np.isclose(norm, 1.0):
        raise ValueError("State must be normalized")

    if basis == "Z":
        measurement_state = state

    elif basis == "X":
        measurement_state = H @ state

    else:
        raise ValueError("Basis must be Z or X")

    probabilities = np.abs(measurement_state) ** 2
    probabilities = probabilities / probabilities.sum()

    if rng is None:
        rng = np.random.default_rng()

    result = int(rng.choice([0, 1], p=probabilities))

    collapsed_state = (
        ZERO.copy() if result == 0 else ONE.copy()
    )

    if basis == "X":
        collapsed_state = H @ collapsed_state

    return result, collapsed_state
