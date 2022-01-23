import unittest

from ..problems.week1_1 import solve as solve1
from ..problems.week1_2 import solve as solve2


class TestWeek1(unittest.TestCase):
    def test_week1_1(self) -> None:
        a = 9
        b = 7
        ans = 16

        self.assertEqual(solve1(a, b), ans)

    def test_week1_2(self) -> None:
        n1 = [1, 2, 3]
        ans1 = 6

        n2 = [5, 6, 2, 7, 4]
        ans2 = 42

        self.assertEqual(solve2(n1), ans1)
        self.assertEqual(solve2(n2), ans2)
