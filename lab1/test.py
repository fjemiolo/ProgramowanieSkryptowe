import main
import unittest
from fractions import Fraction


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(Exception):
            main.sum(2, 'Ala ma kota123')

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(7, 8), Fraction(1, 4)), Fraction(9, 8))

    def test_sum_fraction_float_string(self):
        self.assertEqual(main.sum(Fraction(4, 3), "5.0"), 6.3333333333333334)

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(5, 3), complex(1, 8)), complex(6, 11))

    def test_sum_wrong_argument(self):
        with self.assertRaises(Exception):
            main.sum(1, [2, 3])


if __name__ == '__main__':
    unittest.main()