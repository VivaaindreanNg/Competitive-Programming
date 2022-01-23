import unittest

from ..problems.week3_1 import solve as solve1


class TestWeek3(unittest.TestCase):
    def test_week3_1(self) -> None:
        num1 = 2
        ans1 = 2  # 1 + 1

        num2 = 28
        ans2 = 6  # 10 + 10 + 5 + 1 + 1 + 1

        num3 = 11
        ans3 = 2  # 10 + 1

        self.assertEqual(solve1(num1, 0), ans1)
        self.assertEqual(solve1(num2, 0), ans2)
        self.assertEqual(solve1(num3, 0), ans3)
