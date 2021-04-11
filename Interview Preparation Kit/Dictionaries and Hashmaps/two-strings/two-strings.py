def twoStrings(s1: str, s2: str) -> str:
    """
    :param s1: a string
    :param s2: another string
    :return: either "YES" or "NO"
    """
    if set.intersection(set(s1), set(s2)):
        return "YES"

    return "NO"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        print(twoStrings(input(), input()))
