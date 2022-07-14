import unittest


class TestSkippingStuf(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1+1, 2)

    def test_subtraction(self):
        self.assertEqual(10-5, 5)

    @unittest.skip('T o be implemented later')
    def test_multiplication(self):
        pass


if __name__ == '__main__':
    unittest.main()
