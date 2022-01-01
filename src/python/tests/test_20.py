

import unittest

from ..problems.problem_20 import solve


class Test20(unittest.TestCase):

    def test(self) -> None:
        n = 10
        ans = 3628800
        self.assertEqual(solve(n), ans)