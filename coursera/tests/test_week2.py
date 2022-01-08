from ..problems.week2_1 import solve as solve1

import unittest


class TestWeek2(unittest.TestCase):
    def test_week2_1(self) -> None:
        num1 = 3
        ans1 = 2

        num2 = 10
        ans2 = 55

        self.assertEqual(solve1(num1), ans1)
        self.assertEqual(solve1(num2), ans2)
