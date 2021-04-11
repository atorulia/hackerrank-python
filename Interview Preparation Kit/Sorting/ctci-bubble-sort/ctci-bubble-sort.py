from typing import List


def countSwaps(a: List[int]):
    """
    :param a: an array of integers to sort
    :return: Print the three lines required, then return. No return value is expected.
    """
    count_swaps = 0

    while not all(first_item <= second_item for first_item, second_item in zip(a, a[1:])):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count_swaps += 1

    print(f"Array is sorted in {count_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a) - 1]}")


if __name__ == '__main__':
    n = int(input())
    countSwaps(list(map(int, input().rstrip().split())))