def alternatingCharacters(s: str) -> int:
    """
    :param s: a string
    :return: the minimum number of deletions required
    """
    deletions_required = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions_required += 1

    return deletions_required


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        print(alternatingCharacters(input()))
