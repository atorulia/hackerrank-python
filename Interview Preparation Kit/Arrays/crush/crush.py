from typing import List


def arrayManipulation(n: int, queries: List[List[int]]):
    """
    :param n: the number of elements in the array
    :param queries: a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
    :return: the maximum value in the resultant array
    """
    arr = [0] * n

    for query in queries:
        a, b, k = query
        # adds "k" to all subsequent elements in the array
        arr[a - 1] += k

        # ignore if b is out of range
        if b < n:
            # subtracts "k" from all subsequent elements in the array
            arr[b] -= k

    s = 0
    max_sum = 0

    for item in arr:
        s += item

        max_sum = max(s, max_sum)

    return max_sum


if __name__ == '__main__':
    nm = input().split()

    _n = int(nm[0])

    m = int(nm[1])

    q = []

    for _ in range(m):
        q.append(list(map(int, input().rstrip().split())))

    print(arrayManipulation(_n, q))

