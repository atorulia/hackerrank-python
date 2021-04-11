from collections import defaultdict


def sherlockAndAnagrams(s: str) -> int:
    """
    :param s: a string
    :return: the number of unordered anagrammatic pairs of substrings in s
    """
    # Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the
    # dict class that returns a dictionary-like object. The functionality of both dictionaries and defualtdict
    # are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the
    # key that does not exists.
    substrings = defaultdict(int)

    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            # generate dict of any exist substrings and add 1 if substring already exists
            substrings[''.join(sorted(s[j:j + i]))] += 1

    ans = 0
    for key, value in substrings.items():
        print(key, value)
        ans += value * (value - 1) // 2

    return ans


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        print(sherlockAndAnagrams(input()))

