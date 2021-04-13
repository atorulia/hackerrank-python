def substrCount(n: int, s: str) -> int:
    """
    :param n: the length of string s
    :param s: a string
    :return: the number of special substrings
    """
    line = []
    count = 0
    current = None

    for i in range(n):
        if s[i] == current:
            count += 1
        else:
            if current is not None:
                line.append((current, count))
            current = s[i]
            count = 1

    line.append((current, count))

    substr_count = 0

    for substr in line:
        substr_count += (substr[1] * (substr[1] + 1)) // 2

    for i in range(1, len(line) - 1):
        if line[i - 1][0] == line[i + 1][0] and line[i][1] == 1:
            substr_count += min(line[i - 1][1], line[i + 1][1])

    return substr_count


if __name__ == '__main__':
    print(substrCount(int(input()), input()))
