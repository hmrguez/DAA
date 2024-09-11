import random
import unittest
from brute_force import brute_force_numbness
from solution import solve


class TestSolutions(unittest.TestCase):
    def generate_random_array(self, n, max_value=1000, seed=None):
        if seed is not None:
            random.seed(1000)
        return [random.randint(0, max_value) for _ in range(n)]

    def test_solutions(self):
        num_tests = 10
        max_n = 100  # Maximum size of the array
        max_value = 1000  # Maximum value of elements in the array

        for i in range(num_tests):
            n = random.randint(1, max_n)
            a = self.generate_random_array(n, max_value)

            # Add a leading zero to match the input format of the solve function
            a_with_leading_zero = [0] + a

            # Get the results from both methods
            brute_force_result = brute_force_numbness(n, a)
            optimized_result = solve(n, a_with_leading_zero)

            # Compare the results
            self.assertEqual(brute_force_result, optimized_result,
                             f"Test failed for array: {a}\nBrute force result: {brute_force_result}\nOptimized result: {optimized_result}")


if __name__ == "__main__":
    unittest.main()
