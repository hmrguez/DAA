import copy
import unittest
from parameterized import parameterized
from solution import solve as my_solution
from brute_force import solve as brute_force_solution

n1, k1 = 3, 4
o1 = 21
a1 = [5, 6, 7]
b1 = [2, 3, 4]

n2, k2 = 5, 9
o2 = 349
a2 = [32, 52, 68, 64, 14]
b2 = [18, 14, 53, 24, 8]

n3, k3 = 5, 1000
o3 = 27
a3 = [1, 2, 3, 4, 5]
b3 = [5, 4, 3, 2, 1]

n4, k4 = 10, 6
o4 = 47
a4 = [3, 3, 5, 10, 6, 8, 6, 8, 7, 7]
b4 = [6, 1, 7, 4, 1, 1, 8, 9, 3, 1]


class TestProblem1(unittest.TestCase):
    @parameterized.expand([
        (a1, b1, n1, k1),
        (a2, b2, n2, k2),
        (a3, b3, n3, k3),
        (a4, b4, n4, k4),
    ])
    def test_solutions(self, a, b, n, k):
        a_copy = copy.deepcopy(a)
        b_copy = copy.deepcopy(b)

        self.assertEqual(brute_force_solution(a_copy, b_copy, n, k), my_solution(a, b, n, k))


if __name__ == '__main__':
    unittest.main()
