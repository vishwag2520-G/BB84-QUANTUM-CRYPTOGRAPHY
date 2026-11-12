import secrets
from bb84.quantum import measure_qubit


def generate_bases(n):
    """Generate Bob's independent random bases."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    return [
        "Z" if secrets.randbits(1) == 0 else "X"
        for _ in range(n)
    ]


def measure_states(states, bases):
    """Measure received quantum states."""
    if len(states) != len(bases):
        raise ValueError("States and bases must have equal length")

    results = []

    for state, basis in zip(states, bases):
        result, _ = measure_qubit(state, basis)
        results.append(result)

    return results


def bob_simulation(states):
    """Run Bob's complete measurement process."""
    bases = generate_bases(len(states))
    results = measure_states(states, bases)

    return bases, results

    return indices, alice_key, bob_ke