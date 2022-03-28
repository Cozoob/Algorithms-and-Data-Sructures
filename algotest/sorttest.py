import unittest

from algo import sort


class MyTestCase(unittest.TestCase):
    def test_max_sub_sum(self):
        arr = [7, -10, 2, 5, 3, -1, 8, -100, 2]
        self.assertEqual(17, sort.max_sub_sum1(arr, 0, len(arr) - 1))

        self.assertEqual(17, sort.max_sub_sum2(arr))

        arr = [-1, -1, -1, -1]
        self.assertEqual(0, sort.max_sub_sum1(arr, 0, len(arr) - 1))
        self.assertEqual(0, sort.max_sub_sum2(arr))

        arr = [100, 100, 1000, -1000000, 456]
        self.assertEqual(1200, sort.max_sub_sum1(arr, 0, len(arr) - 1))
        self.assertEqual(1200, sort.max_sub_sum2(arr))

        arr = [100, 100, 1000, -1000000, 100000000]
        self.assertEqual(100000000, sort.max_sub_sum1(arr, 0, len(arr) - 1))
        self.assertEqual(100000000, sort.max_sub_sum2(arr))


if __name__ == '__main__':
    unittest.main()
