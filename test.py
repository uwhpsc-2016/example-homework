import unittest

from example_homework import square

class TestSquare(unittest.TestCase):
    def setUp(self):
        pass

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_one(self):
        self.assertEqual(square(1), 1)

    def test_two_three_four(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)

    def test_negative(self):
        self.assertEqual(square(-1), 1)

if __name__ == '__main__':
    unittest.main()
