from typing import List


def maximumToys(prices: List[int], k: int) -> int:
    """
    :param prices: the toy prices
    :param k: Mark's budget
    :return: the maximum number of toys
    """
    maximum_toys = 0

    prices.sort()
    for maximum_toys in range(len(prices)):
        if k > prices[maximum_toys]:
            k -= prices[maximum_toys]
        else:
            break

    return maximum_toys


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    amount = int(nk[1])

    print(maximumToys(list(map(int, input().rstrip().split())), amount))
