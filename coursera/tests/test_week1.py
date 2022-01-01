from ..problems.week1_1 import solve as solve1
from ..problems.week1_2 import solve as solve2

import unittest

class TestWeek1(unittest.TestCase):

    def test_week1_1(self) -> None:
        a = 9
        b = 7
        ans = 16

        self.assertEqual(solve1(a, b), ans)

    def test_week1_2(self) -> None:
        n = 3
        a, b, c = 1, 2, 3
        ans = 6

        self.assertEqual(solve2(n, a, b, c), ans)
