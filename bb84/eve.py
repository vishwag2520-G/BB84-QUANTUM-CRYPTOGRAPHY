import secrets
from bb84.quantum import measure_qubit, encode_qubit


def generate_eve_bases(n):
    """Generate Eve's random measurement bases."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return [
        "Z" if secrets.randbits(1) == 0 else "X"
        for _ in range(n)
    ]


def intercept_and_resend(states):
    """Simulate Eve's intercept-and-resend attack."""

    eve_bases = generate_eve_bases(len(states))

    eve_results = []
    resent_states = []

    for state, basis in zip(states, eve_bases):
        result, _ = measure_qubit(state, basis)

        eve_results.append(result)

        resent_state = encode_qubit(result, basis)
        resent_states.append(resent_state)

    return eve_bases, eve_results, resent_states
