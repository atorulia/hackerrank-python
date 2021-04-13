from collections import Counter


def is_all_valid(counter: Counter) -> bool:
    """
    :param counter: frequency counter
    :return: string valid status
    """
    values = list(counter.values())
    try:
        values.remove(0)
    except:
        pass

    if len(set(values)) == 1:
        return True
    else:
        return False


def isValid(s: str) -> str:
    """
    :param s: a string
    :return: either YES or NO
    """
    frequency = Counter(s)

    if is_all_valid(frequency):
        return "YES"

    for key in frequency.keys():
        frequency[key] -= 1
        if is_all_valid(frequency):
            return "YES"
        else:
            frequency[key] += 1

    return "NO"


if __name__ == '__main__':
    print(isValid(input()))
