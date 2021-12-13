import unittest
from lib import p3

class Test_FlourOrder(unittest.TestCase):
    def test_1(self):
        result = p3.flour_order(1,1,1,1)
        expected_result = [2, "A", 58200]
        self.assertEqual(result, expected_result)

    def test_2_equal_2kg(self):
        result = p3.flour_order_2(1,1,1,1)
        expected_result = (2, "A", 58200)
        self.assertEqual(result, expected_result)

    def test_2_equal_30kg(self):
        result = p3.flour_order_2(0,60,0,0)
        expected_result = (30, "A", 855000)
        self.assertEqual(result, expected_result)

    def test_2_equal_40kg(self):
        result = p3.flour_order_2(0,80,0,0)
        expected_result = (40, "B", 1116000)
        self.assertEqual(result, expected_result)


    def test_2_equal_45kg(self):
        result = p3.flour_order_2(0,90,0,0)
        expected_result = (46, "B", 1283400)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
