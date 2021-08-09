# As part of the CI, you will create a simple unit test
# (very simple one, that checks 2 + 2 = 4 e.g.)
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        assert sum([2, 2]) == 4
