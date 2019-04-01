import unittest
import check_strings

class TestCheckStrings(unittest.TestCase):
    def test_compare_strings(self):
        self.assertEqual(check_strings.compare_strings(4, 5), '4.0 is lesser than 5.0')
        self.assertEqual(check_strings.compare_strings(7, 5), '7.0 is greater than 5.0')
        self.assertEqual(check_strings.compare_strings(5, 5), '5.0 is equal to 5.0')

        self.assertEqual(check_strings.compare_strings(-4, -5), '-4.0 is greater than -5.0')
        self.assertEqual(check_strings.compare_strings(-7, -5), '-7.0 is lesser than -5.0')
        self.assertEqual(check_strings.compare_strings(-5.9, -5.9), '-5.9 is equal to -5.9')


if __name__ == '__main__':
    unittest.main()