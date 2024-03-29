import unittest

from algo import sort
from random import randint


def get_random_arr():
    return [randint(-30, 100) for _ in range(randint(4, 40))]

def get_random_arr_for_counting_sort():
    return [randint(0, 20) for _ in range(randint(4, 40))]

def get_random_arr_for_radix_sort():
    return [randint(0, 10000) for _ in range(randint(10, 40))]

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

    def test_binary_search(self):
        arr = [-5, 20, 26, 38, 40, 43, 45, 49, 59, 78, 89, 90]
        self.assertEqual(1, sort.binary_search1(arr, 0, len(arr) - 1, 20))
        self.assertEqual(1, sort.binary_search2(arr, 20))

        self.assertEqual(8, sort.binary_search1(arr, 0, len(arr) - 1, 59))
        self.assertEqual(8, sort.binary_search2(arr, 59))

        self.assertEqual(11, sort.binary_search1(arr, 0, len(arr) - 1, 90))
        self.assertEqual(11, sort.binary_search2(arr, 90))

        self.assertEqual(-1, sort.binary_search1(arr, 0, len(arr) - 1, -90))
        self.assertEqual(-1, sort.binary_search2(arr, -90))

        self.assertEqual(0, sort.binary_search1(arr, 0, len(arr) - 1, -5))
        self.assertEqual(0, sort.binary_search2(arr, -5))

    def test_merge_sort(self):
        for _ in range(5):
            arr1 = get_random_arr()
            arr2 = arr1.copy()
            sort.merge_sort(arr1, 0, len(arr1) - 1)
            arr2.sort()

            self.assertEqual(arr2, arr1)

    def test_quick_sort(self):
        for _ in range(5):
            arr1 = get_random_arr()
            arr2 = arr1.copy()
            sort.quick_sort(arr1, 0, len(arr1) - 1)
            arr2.sort()

            self.assertEqual(arr1, arr2)

    def test_counting_sort(self):
        for _ in range(5):
            arr1 = get_random_arr_for_counting_sort()
            arr2 = arr1.copy()
            sort.counting_sort(arr1)
            arr2.sort()

            self.assertEqual(arr1, arr2)

    def test_bucket_sort(self):
        arr1 = [9, 1, 4, 56, 23, 5, 1, 0, 23, 12, 7, -100, -23, 5]
        arr2 = arr1.copy()
        sort.bucket_sort(arr1)
        arr2.sort()

        self.assertEqual(arr1, arr2)

        arr1 = [0.41, 0.42, 0.13, 0.07, 0.21, 0.91, 0.13, 0.37]
        arr2 = arr1.copy()
        sort.bucket_sort(arr1)
        arr2.sort()

        self.assertEqual(arr1, arr2)

    def test_select(self):
        for _ in range(5):
            arr = get_random_arr()
            k = randint(0, len(arr) - 1)
            number = sort.select(arr, 0, len(arr) - 1, k)
            arr.sort()

            while arr[k] == arr[k - 1] and k > 1:
                k -= 1

            self.assertEqual(arr.index(number), k)



    def test_radix_sort(self):
        for _ in range(5):
            arr1 = get_random_arr_for_radix_sort()
            arr2 = arr1.copy()
            arr1.sort()
            sort.radix_sort(arr2)

            self.assertEqual(arr1, arr2)

    def test_heap_sort(self):
        for _ in range(5):
            arr1 = get_random_arr()
            arr2 = arr1.copy()
            arr1.sort()
            sort.max_heap_sort(arr2)

            self.assertEqual(arr1, arr2)

        for _ in range(5):
            arr1 = get_random_arr()
            arr2 = arr1.copy()
            arr1.sort()
            arr1.reverse()
            sort.min_heap_sort(arr2)

            self.assertEqual(arr1, arr2)

if __name__ == '__main__':
    unittest.main()
