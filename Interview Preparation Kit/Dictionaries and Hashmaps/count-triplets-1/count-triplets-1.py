from collections import defaultdict
from typing import List


def countTriplets(arr: List[int], r: int) -> int:
    """
    :param arr: an array of integers
    :param r: the common ratio
    :return: the number of triplets
    """
    v3 = defaultdict(int)
    v2 = defaultdict(int)
    count = 0

    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1

    return count


if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    ratio = int(nr[1])

    countTriplets(list(map(int, input().rstrip().split())), ratio)
