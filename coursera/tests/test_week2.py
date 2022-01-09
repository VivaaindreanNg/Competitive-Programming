from ..problems.week2_1 import solve1, solve2

import time
import unittest


class TestWeek2(unittest.TestCase):
    def test_week2_1(self) -> None:
        num1 = 3
        ans1 = 2

        num2 = 10
        ans2 = 55

        self.assertEqual(solve1(num1), ans1)
        self.assertEqual(solve1(num2), ans2)

    def test_week2_1_memoization(self) -> None:
        num3 = 40
        ans3 = 102334155

        start1 = time.time()
        self.assertEqual(solve1(num3), ans3)
        end1 = time.time()
        time1 = end1 - start1

        start2 = time.time()
        self.assertEqual(solve2(num3), ans3)
        end2 = time.time()
        time2 = end2 - start2

        self.assertGreater(time1, time2)
