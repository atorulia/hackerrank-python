from typing import List


def minimumAbsoluteDifference(arr: List[int]) -> int:
    """
    :param arr: an array of integers
    :return: the minimum absolute difference found
    """
    _arr = sorted(arr)

    return min(map(lambda item: abs(item[0] - item[1]), zip(_arr[1:], _arr)))


if __name__ == '__main__':
    n = int(input())
    print(minimumAbsoluteDifference(arr=list(map(int, input().rstrip().split()))))
