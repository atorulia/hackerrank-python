from typing import List


def jumpingOnClouds(c: List[int]) -> int:
    """
    :param c: an array of binary integers
    :return: the minimum number of jumps required
    """
    clouds_length = len(c)
    jumps, position = 0, 0

    while position < clouds_length - 1:
        position += 2 if position < clouds_length - 2 and not c[position + 2] else 1
        jumps += 1

    return jumps


if __name__ == '__main__':
    input()
    print(jumpingOnClouds(list(map(int, input().strip().split()))))
