from typing import List, Tuple


def mergeSort(arr: List[int]) -> Tuple[List[int], int]:
    arr_length = len(arr)

    if arr_length <= 1:
        return arr, 0

    count_inversions = 0

    left_arr, left_inversions = mergeSort(arr[:int(arr_length / 2)])
    right_arr, right_inversions = mergeSort(arr[int(arr_length / 2):])

    merged_arr = []
    i, j = 0, 0
    len_left, len_right = len(left_arr), len(right_arr)

    for k in range(arr_length - 1):
        if i == len_left or j == len_right:
            break

        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1
            count_inversions += len_left - i

    merged_arr += left_arr[i:]
    merged_arr += right_arr[j:]

    return merged_arr, sum([count_inversions, left_inversions, right_inversions])


def countInversions(arr: List[int]) -> int:
    """
    :param arr: an array of integers to sort
    :return: the number of inversions
    """
    sorted_arr, count_inversions = mergeSort(arr)
    return count_inversions


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        print(countInversions(list(map(int, input().rstrip().split()))))
