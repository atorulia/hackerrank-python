from typing import List
from collections import Counter


def checkMagazine(magazine: List[str], note: List[str]) -> None:
    """
    :param magazine: the words in the magazine
    :param note: the words in the ransom note
    :return: string: either "Yes" or "No", no return value is expected
    """
    if Counter(note) - Counter(magazine):
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    checkMagazine(input().rstrip().split(), input().rstrip().split())
