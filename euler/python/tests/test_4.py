from ..problems.problem_4 import solve

import unittest


class Test3(unittest.TestCase):
    def test(self) -> None:
        n1 = 2 
        ans1 = 9009

        n2 = 3
        ans2 = 906609

        self.assertEqual(solve(n1), ans1)
        self.assertEqual(solve(n2), ans2)