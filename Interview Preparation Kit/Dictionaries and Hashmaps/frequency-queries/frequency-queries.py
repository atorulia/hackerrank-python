from collections import defaultdict
from typing import List


def freqQuery(queries: List[int]) -> List[int]:
    """
    :param queries: a 2-d array of integers
    :return: the results of queries of type 3
    """
    results = []
    quantities = dict()
    frequencies = defaultdict(set)

    for command, value in queries:
        frequency = quantities.get(value, 0)
        if command == 1:
            quantities[value] = frequency + 1
            frequencies[frequency].discard(value)
            frequencies[frequency + 1].add(value)
        elif command == 2:
            quantities[value] = max(0, frequency - 1)
            frequencies[frequency].discard(value)
            frequencies[frequency - 1].add(value)
        elif command == 3:
            results.append(1 if frequencies[value] else 0)
        else:
            raise Exception("Query type out of query types")
    return results


if __name__ == '__main__':
    q = []

    for _ in range(int(input().strip())):
        q.append(list(map(int, input().rstrip().split())))

    print(freqQuery(q))

