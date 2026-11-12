def compare_bases(alice_bases, bob_bases):
    if len(alice_bases) != len(bob_bases):
        raise ValueError("Basis lengths must match")

    return [
        i for i, (a, b) in enumerate(
            zip(alice_bases, bob_bases)
        )
        if a == b
    ]


def sift_key(bits, matching_indices):
    return [bits[i] for i in matching_indices]


def generate_sifted_keys(
    alice_bits, bob_results, alice_bases, bob_bases
):
    if not (
        len(alice_bits) == len(bob_results)
        == len(alice_bases) == len(bob_bases)
    ):
        raise ValueError("All input lengths must match")

    indices = compare_bases(alice_bases, bob_bases)

    alice_key = sift_key(alice_bits, indices)
    bob_key = sift_key(bob_results, indices)

    return indices, alice_key, bob_key
