from collections import Counter


def makeAnagram(a: str, b: str) -> int:
    """
    :param a: a string
    :param b: another string
    :return: the minimum total characters that must be deleted
    """

    a_counter = Counter(a)
    b_counter = Counter(b)

    a_counter.subtract(b_counter)
    minimum_total = 0

    for key in a_counter:
        minimum_total += abs(a_counter[key])

    return minimum_total


if __name__ == '__main__':
    print(makeAnagram(input(), input()))
