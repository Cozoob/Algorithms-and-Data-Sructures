"""
    The library of sorting algorithms and some other
    related to them algos.
"""


def max_sub_sum1(arr: [int], start: int, end: int) -> int:
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
        return max(0, arr[start])

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


def max_sub_sum2(arr: [int]):
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


def binary_search1(arr: [int], left: int, right: int, number: int):
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


def binary_search2(arr: [int], number: int):
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
