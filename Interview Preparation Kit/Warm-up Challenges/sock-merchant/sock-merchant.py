from typing import List


def sockMerchant(n: int, ar: List[int]):
    """
    :param n: the number of socks in the pile
    :param ar: the colors of each sock
    :return: the number of pairs
    """
    line = list(set(ar))
    score = 0

    for i in range(len(line)):
        score += ar.count(line[i]) // 2
    return score


if __name__ == '__main__':
    print(sockMerchant(int(input()), list(map(int, input().strip().split()))))
