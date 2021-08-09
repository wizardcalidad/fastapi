import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        assert sum([2, 2]) == 4
