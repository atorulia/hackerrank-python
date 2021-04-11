from bisect import bisect_left, insort_left
from typing import List


def median(arr: List[int], days: int) -> int:
    """
    :return: median of arr
    """
    return arr[days // 2] if days % 2 else ((arr[days // 2] + arr[days // 2 - 1]) / 2)


def activityNotifications(expenditure: List[int], d: int) -> int:
    """
    :param expenditure: daily expenditures
    :param d: the lookback days for median spending
    :return: the number of notices sent
    """
    notifications = 0
    heap = sorted(expenditure[:d])

    for i in range(d, len(expenditure) - 1):
        if expenditure[i] >= 2 * median(heap, d):
            notifications += 1

        del heap[bisect_left(heap, expenditure[i-d])]
        insort_left(heap, expenditure[i])

    return notifications


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    _days = int(nd[1])

    print(activityNotifications(list(map(int, input().rstrip().split())), _days))
