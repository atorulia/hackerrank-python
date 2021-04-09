from typing import List


def minimumSwaps(arr: List[int]):
    """
    :param arr: an unordered array of integers
    :return: the minimum number of swaps to sort the array
    """
    swaps = 0

    for i in range(len(arr) - 1):
        while arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            swaps += 1

    return swaps


if __name__ == '__main__':
    n = int(input())

    print(minimumSwaps(list(map(int, input().rstrip().split()))))
