import sys
import unittest

from lib import p1



class Test_FindSplit80(unittest.TestCase):
    def test_1(self):
        list = range(0, 20)
        test = p1.find_split_80(list)
        expected_result = 17
        self.assertEqual(test, expected_result)

    def test_2(self):
        

if __name__ == '__main__':

    unittest.main(verbosity=2)
