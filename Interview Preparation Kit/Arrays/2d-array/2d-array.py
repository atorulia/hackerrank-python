from typing import List


def hourglassSum(arr: List[List[int]]) -> int:
    """
    :param arr: an array of integers
    :return:  the maximum hourglass sum
    """
    hourglass_sum = -63  # the minimal sum

    for i in range(4):
        for j in range(4):
            hourglass_sum = max(hourglass_sum, sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))

    return hourglass_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
