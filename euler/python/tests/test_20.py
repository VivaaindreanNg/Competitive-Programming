import unittest

from ..problems.problem_20 import solve


class Test20(unittest.TestCase):
    def test(self) -> None:
        n1 = 10
        ans1 = 27

        n2 = 100
        ans2 = 648

        self.assertEqual(solve(n1), ans1)
        self.assertEqual(solve(n2), ans2)
