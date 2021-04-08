def countingValleys(steps: int, path: str) -> int:
    """
    :param steps: the number of steps on the hike
    :param path: a string describing the path
    :return: the number of valleys traversed
    """
    level, valleys = 0, 0

    for i in range(steps):
        if path[i] == 'U':
            level += 1

            if not level:
                valleys += 1
        else:
            level -= 1

    return valleys


if __name__ == '__main__':
    print(countingValleys(int(input()), str(input())))



