import sys
import unittest

from lib import p2

class Test_EstimatePi(unittest.TestCase):
    def test_1(self):
        result = p2.estimate_pi(10000)
        test = 3.14
        deviation = abs(test - result)
        self.assertTrue(deviation < 0.01)

    def test_2(self):
        result = p2.estimate_pi_2(1000000)
        test = 3.14
        deviation = abs(test - result)
        self.assertTrue(deviation < 0.01)

if __name__ == '__main__':
    unittest.main(verbosity=2)
