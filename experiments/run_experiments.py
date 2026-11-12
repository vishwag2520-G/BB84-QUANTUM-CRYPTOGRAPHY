
import os
import matplotlib.pyplot as plt

from bb84.alice import alice_simulation
from bb84.bob import bob_simulation
from bb84.eve import intercept_and_resend
from bb84.sifting import generate_sifted_keys
from bb84.security import calculate_qber


def run_experiment(n=10000):

    # Experiment 1: Without Eve
    bits, alice_bases, states = alice_simulation(n)
    bob_bases, bob_results = bob_simulation(states)

    _, alice_key, bob_key = generate_sifted_keys(
        bits, bob_results, alice_bases, bob_bases
    )

    errors, total, qber = calculate_qber(
        alice_key, bob_key
    )

    qber_no_eve = qber

    print("\n--- WITHOUT EVE ---")
    print("Sifted bits:", total)
    print("Errors:", errors)
    print("QBER:", round(qber, 2), "%")

    # Experiment 2: With Eve
    bits, alice_bases, states = alice_simulation(n)
    _, _, resent_states = intercept_and_resend(states)

    bob_bases, bob_results = bob_simulation(resent_states)

    _, alice_key, bob_key = generate_sifted_keys(
        bits, bob_results, alice_bases, bob_bases
    )

    errors, total, qber = calculate_qber(
        alice_key, bob_key
    )

    qber_with_eve = qber

    print("\n--- WITH EVE ---")
    print("Sifted bits:", total)
    print("Errors:", errors)
    print("QBER:", round(qber, 2), "%")

    # Visualization
    os.makedirs("results", exist_ok=True)

    labels = ["Without Eve", "With Eve"]
    values = [qber_no_eve, qber_with_eve]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)

    plt.axhline(
        y=25,
        linestyle="--",
        label="Theoretical attack QBER (25%)"
    )

    plt.ylabel("Quantum Bit Error Rate (%)")
    plt.title("BB84: Impact of Intercept-and-Resend Attack")
    plt.ylim(0, 35)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "results/qber_comparison.png",
        dpi=300
    )

    plt.close()

    print("\nChart saved: results/qber_comparison.png")


if __name__ == "__main__":
    run_experiment()
