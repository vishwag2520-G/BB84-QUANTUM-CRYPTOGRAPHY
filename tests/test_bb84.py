import unittest
import numpy as np

from bb84.quantum import encode_qubit, measure_qubit
from bb84.alice import generate_bits, generate_bases
from bb84.sifting import compare_bases
from bb84.security import calculate_qber


class TestBB84(unittest.TestCase):

    def test_encode_z_basis(self):
        state = encode_qubit(0, "Z")
        np.testing.assert_array_equal(state, [1, 0])

    def test_encode_x_basis(self):
        state = encode_qubit(0, "X")
        expected = np.array([1, 1]) / np.sqrt(2)
        np.testing.assert_allclose(state, expected)

    def test_measurement(self):
        state = encode_qubit(1, "Z")
        result, _ = measure_qubit(state, "Z")
        self.assertEqual(result, 1)

    def test_generate_bits(self):
        bits = generate_bits(100)
        self.assertEqual(len(bits), 100)
        self.assertTrue(all(bit in (0, 1) for bit in bits))

    def test_generate_bases(self):
        bases = generate_bases(100)
        self.assertEqual(len(bases), 100)
        self.assertTrue(all(basis in ("Z", "X") for basis in bases))

    def test_basis_comparison(self):
        alice = ["Z", "X", "Z", "X"]
        bob = ["Z", "Z", "Z", "X"]
        self.assertEqual(compare_bases(alice, bob), [0, 2, 3])

    def test_qber(self):
        alice = [0, 1, 1, 0]
        bob = [0, 0, 1, 1]
        errors, total, qber = calculate_qber(alice, bob)

        self.assertEqual(errors, 2)
        self.assertEqual(total, 4)
        self.assertEqual(qber, 50.0)


if __name__ == "__main__":
    unittest.main()
