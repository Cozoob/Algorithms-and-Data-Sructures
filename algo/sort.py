"""
    The library of sorting algorithms and some other
    related to them algos.
"""


def max_sub_sum1(arr: list[float], start: int, end: int) -> float:
    """
    Finds the maximum subsequence sum of given array.
    Algorithm uses recursive approach.

    Time: O(nlogn)

    :param arr: The array with numbers to find the maximum subsequence sum.
    :param start: The starting index of summing.
    :param end: The ending index of summing.
    :return: The sum of the maximum subsequence sum in array.
    """
    size = end - start + 1
    middle = start + (end - start) // 2

    if size == 0:
        return 0

    # if the sum is smaller than 0, ignore the sum.
    if size == 1:
        return arr[start] if arr[start] >= 0 else 0

    result_left = max_sub_sum1(arr, start, middle)
    result_right = max_sub_sum1(arr, middle + 1, end)

    span_left, span_right, partial = 0, 0, 0

    for i in range(middle - 1, start - 1, -1):
        partial += arr[i]
        span_left = max(partial, span_left)

    partial = 0

    for i in range(middle, end + 1):
        partial += arr[i]
        span_right = max(partial, span_right)

    return max(result_left, result_right, span_left + span_right)


def max_sub_sum2(arr: list[float]) -> float:
    """
    Finds the maximum subsequence sum of given array.
    Sum the numbers from the start and remember the best result.
    If the sum is smaller than 0, forget the value of sum and sum again.
    The result also allows summing nothing then 0 is a correct answer.

    Time: O(n)

    Function: f(i) - max value of the result that ends on i-th element.

    f(i) = max(f(i-1) + arr[i], 0)

    :param arr: The array of numbers to find the maximum subsequence sum.
    :return: The sum of the maximum subsequence.
    """
    result = 0
    partial = 0
    size = len(arr)

    for i in range(size):
        partial += arr[i]
        partial = max(0, partial)
        result = max(result, partial)

    return result


def binary_search1(arr: list[float], left: int, right: int, number: int) -> int:
    """
    Finds the index of the number (element) in the sorted array.

    Algorithm uses recursive approach.

    Time: O(logn)

    :param arr: The sorted array.
    :param left: The starting index.
    :param right: The ending index.
    :param number: The element to find its index.
    :return: The index of the number in array. If not found, returns -1.
    """

    if left > right:
        return -1

    middle = left + (right - left) // 2

    if arr[middle] == number:
        return middle
    elif arr[middle] < number:
        return binary_search1(arr, middle + 1, right, number)
    else:
        # arr[middle] > number
        return binary_search1(arr, left, middle - 1, number)


def binary_search2(arr: list[float], number: int) -> int:
    """
    Finds the index of the number (element) in the sorted array.

    Algorithm uses iterative approach.

    Time: O(logn)

    :param arr: The sorted array.
    :param number: The element to find its index.
    :return: The index of the number in array. If not found, returns -1.
    """
    left, right = 0, len(arr)

    while left <= right:
        middle = left + (right - left) // 2

        if arr[middle] == number:
            return middle
        elif arr[middle] > number:
            right = middle - 1
        else:
            # arr[middle] < number
            left = middle + 1

    return -1


def merge_sort(arr: list[float], start: int, end: int):
    """
    Sorts the array of the numbers.

    Stable: Yes.

    Time: O(nlogn)

    Space: O(n), but actually in Python in this implementation
    it's more...

    Algorithm uses the recursive approach.

    :param arr: The array of numbers to sort.
    :param start: The starting index.
    :param end: The ending index.
    :return: Nothing.
    """

    if start >= end:
        return

    middle = start + (end - start) // 2

    merge_sort(arr, start, middle)
    merge_sort(arr, middle + 1, end)

    left_size = middle - start + 1
    right_size = end - middle

    left_arr = [0.0 for _ in range(left_size)]
    right_arr = [0.0 for _ in range(right_size)]

    for i in range(left_size):
        left_arr[i] = arr[start + i]

    for i in range(right_size):
        right_arr[i] = arr[middle + 1 + i]

    i, j = 0, 0

    for k in range(start, end + 1):
        if i >= left_size:
            # The left array has ended.
            arr[k] = right_arr[j]
            j += 1
        elif j >= right_size:
            # The right array has ended.
            arr[k] = left_arr[i]
            i += 1
        elif left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1


def partition(arr: list[float], start: int, end: int) -> int:
    """
    Makes partition of the array. Function divide
    array for two "subarrays" where first one
    contains the elements smaller than pivot
    and the second one vice versa. The pivot is between these
    "subarrays" at the end. It returns the index of the pivot
    after dividing.

    The function is used in quick sort algorithm.

    :param arr: The array of numbers to make partition.
    :param start: The starting index.
    :param end: The ending index.
    :return: The index of the pivot after partitioning.
    """
    pivot = arr[end]
    i = start

    for j in range(start, end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]

    return i


def quick_sort(arr: list[float], start: int, end: int):
    """
    Sorts the array of the numbers.

    Stable: No.

    Time: O(nlogn) mostly, but can be worse: O(n^2)

    Space: O(1) - don't count the given array.

    :param arr: The array of numbers to sort.
    :param start: The starting index.
    :param end: The ending index.
    :return: Nothing.
    """
    while start < end:
        middle = partition(arr, start, end)
        quick_sort(arr, start, middle - 1)
        start = middle + 1


def counting_sort(arr: list[int]):
    """
    Sorts the array of natural numbers, where
    the largest number cannot be too big!

    Stable: Yes.

    Time: O(n + k), where n - amount of numbers, k - the largest number

    Space: O(n + k), where n - amount of numbers, k - the largest number

    :param arr: The array that contains only natural numbers.
    :return: Nothing.
    """
    n = len(arr)
    largest_number = max(arr)
    counter = [0 for _ in range(largest_number + 1)]
    tmp = [0 for _ in range(n)]

    for i in range(n):
        counter[arr[i]] += 1

    for i in range(1, largest_number + 1):
        counter[i] += counter[i - 1]

    for i in range(n - 1, -1, -1):
        counter[arr[i]] -= 1
        tmp[counter[arr[i]]] = arr[i]

    for i in range(n):
        arr[i] = tmp[i]


def bucket_sort(arr: list[float]):
    """
    Sorts the array of the numbers that are uniform distributed.

    Time: O(n) if there is uniform distribution, else: O(n^2)

    Space: O(n)

    :param arr: The array of the numbers that are uniform distributed.
    :return: Nothing.
    """
    n = len(arr)
    min_value = min(arr)
    max_value = max(arr)
    value_range = (max_value - min_value) / n
    buckets = [[] for _ in range(n)]

    for i in range(n):
        ratio = (arr[i] - min_value) / value_range
        diff = ratio - int(ratio)

        if diff == 0 and arr[i] != min_value:
            buckets[int(ratio) - 1].append(arr[i])
        else:
            buckets[int(ratio)].append(arr[i])

    idx = 0
    for bucket in buckets:
        quick_sort(bucket, 0, len(bucket) - 1)
        for i in range(len(bucket)):
            arr[idx] = bucket[i]
            idx += 1
