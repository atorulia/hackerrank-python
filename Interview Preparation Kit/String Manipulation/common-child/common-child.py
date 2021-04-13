def commonChild(s1: str, s2: str) -> int:
    """
    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    :param s1: a string
    :param s2: another string
    :return: the length of the longest string which is a common child of the input strings
    """
    previous = [0] * (max(len(s1), len(s2)) + 1)

    for i, ai in enumerate(s1):
        current = [0] * (max(len(s1), len(s2)) + 1)
        for j, bj in enumerate(s2):
            if ai == bj:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(current[j - 1], previous[j])
        previous = current
        # print(current)
    return previous[len(s2) - 1]


if __name__ == '__main__':
    print(commonChild(input(), input()))
