import unittest
import figurelib as fl
import math


class Test(unittest.TestCase):
    def test_getFlatSquare(self):
        self.assertEqual(fl.getFlatSquare(10), math.pi * 100)
        self.assertRaises(ValueError, fl.getFlatSquare, -10)
        self.assertAlmostEqual(fl.getFlatSquare(10, 10, 10), 43.3, 2)
        self.assertRaises(ValueError, fl.getFlatSquare, 20, 2, 2)

    def test_isTriangleRight(self):
        self.assertTrue(fl.isTriangleRight(3, 4, 5))
        self.assertFalse(fl.isTriangleRight(10, 10, 10))


if __name__ == '__main__':
    unittest.main()




