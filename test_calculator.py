#https://github.com/StrawberRae007/Lab-11--AR-AC
#Partner 1: Audrey Reid
#Partner 2: Andrea Mae Cecillano

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 2), 6)
        self.assertEqual(mul(-1000, 399), -399000)
        self.assertEqual(mul(4579209, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(5, 50), 10)
        self.assertEqual(div(-1, -1), 1)
        self.assertEqual(div(7,21),3)

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5,10)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(7, 7), 9.9, places=1)
        self.assertAlmostEqual(hypotenuse(-3,-3),4.2, places=1)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(25),5)
        self.assertAlmostEqual(square_root(108),10.4, places=1)

    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-3,4),1)

    def test_subtract(self):
        self.assertEqual(subtract(10,5),5)
        self.assertEqual(subtract(-10,5),-15)
        self.assertEqual(subtract(6,-5),11)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,10)

    def test_logarithm(self):
       self.assertEqual(logarithm(10,100),2)
       self.assertEqual(logarithm(math.e,math.e),1)
       self.assertEqual(logarithm(2,8),3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1,1)
        with self.assertRaises(ValueError):
            logarithm(-5,10)
        with self.assertRaises(ValueError):
            logarithm(0,10)

if __name__ == "__main__":
    unittest.main()
