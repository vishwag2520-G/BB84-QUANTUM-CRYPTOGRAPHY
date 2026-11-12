def calculate_qber(alice_key, bob_key):
    """Calculate the Quantum Bit Error Rate."""

    if len(alice_key) != len(bob_key):
        raise ValueError("Keys must have equal length")

    if len(alice_key) == 0:
        raise ValueError("Keys cannot be empty")

    if any(bit not in (0, 1) for bit in alice_key + bob_key):
        raise ValueError("Keys must contain only binary bits")

    errors = sum(
        a != b for a, b in zip(alice_key, bob_key)
    )

    total_bits = len(alice_key)
    qber = (errors / total_bits) * 100

    return errors, total_bits, qber