from typing import List


def minimumBribes(q: List[int]):
    """
    :param q: the positions of the people after all bribes
    :return:No value is returned. Print the minimum number of bribes necessary or Too chaotic
    if someone has bribed more than 2 people.
    """
    bribes = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        minimumBribes(list(map(int, input().rstrip().split())))
