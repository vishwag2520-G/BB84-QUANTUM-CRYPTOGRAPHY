import secrets
from bb84.quantum import encode_qubit


def generate_bits(n):
    """Generate n cryptographically secure random bits."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")

    return [secrets.randbits(1) for _ in range(n)]

def generate_bases(n):
    """Generate random Z and X measurement bases."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")

    return [
        "Z" if secrets.randbits(1) == 0 else "X"
        for _ in range(n)
    ]


def encode_bits(bits, bases):
    """Encode classical bits into BB84 quantum states."""
    if len(bits) != len(bases):
        raise ValueError("Bits and bases must have equal length")

    return [
        encode_qubit(bit, basis)
        for bit, basis in zip(bits, bases)
    ]


def alice_simulation(n):
    """Run Alice's complete preparation process."""
    bits = generate_bits(n)
    bases = generate_bases(n)
    states = encode_bits(bits, bases)

    return bits, bases, states
