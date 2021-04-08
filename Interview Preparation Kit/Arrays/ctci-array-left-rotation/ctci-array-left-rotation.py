from typing import List


def rotLeft(a: List[int], d: int) -> List[int]:
    """
    :param a: the array to rotate
    :param d: the number of rotations
    :return: the rotated array
    """
    return [a[(d % len(a) + i) % len(a)] for i in range(len(a))]


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(rotLeft(a, d))