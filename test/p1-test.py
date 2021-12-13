import sys
import unittest

from lib import p1

class Test_FindSplit80(unittest.TestCase):
    def test_1(self):
        list = range(0, 20)
        print "\n[test_1] list: ", list
        print "The first 80% are: ", range(0, 16)
        print "The result should be: ", 16
        print "The function return: ", p1.find_split_80(list)
        test = p1.find_split_80(list)
        expected_result = 16
        self.assertEqual(test, expected_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
