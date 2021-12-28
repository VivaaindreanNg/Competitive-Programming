from ..problems.problem_8 import solve

import unittest


class Test8(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test(self) -> None:
        self.assertEqual(0, solve("99"))
