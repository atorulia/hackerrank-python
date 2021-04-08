def repeatedString(s: str, n: int) -> int:
    """
    :param s: a string to repeat
    :param n: the number of characters to consider
    :return: the frequency of a in the substring
    """

    # find count of full string, count of 'a' in start string and find count of 'a' in remainder
    return s.count('a') * (n // len(s)) + (s[:n % len(s)].count('a'))


if __name__ == '__main__':
    print(repeatedString(str(input()), int(input())))
