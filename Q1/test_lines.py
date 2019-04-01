import unittest
import lines

class TestLines(unittest.TestCase):

    def test_check_overlapping(self):
        # if the points resides on positive x-axis
        self.assertEqual(lines.check_overlapping((1, 5), (2, 6)), 'Yes')
        self.assertEqual(lines.check_overlapping((1, 4), (6, 7)), 'No')

        # if the points resides on negative x-axis
        self.assertEqual(lines.check_overlapping((-5, -2), (-3, 6)), 'Yes')
        self.assertEqual(lines.check_overlapping((-5, -2), (-1, 7)), 'No')

        with self.assertRaises(TypeError):
            lines.check_overlapping([1,5], [6,8])

        with self.assertRaises(ValueError):
            lines.check_overlapping((3,), (4,9))

if __name__ == '__main__':
    unittest.main()