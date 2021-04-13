from itertools import groupby


def substrCount(n: int, s: str) -> int:
    """
    :param n: the length of string s
    :param s: a string
    :return: the number of special substrings
    """
    pass


# def k_sum(k):
#     return (k*(k+1))//2
#
#
# def substrCount(n, s):
#     case_a = 0
#     case_b = 0
#     for x,y in groupby(s):
#         case_a += k_sum(sum(1 for i in y))
#     for i in range(1,len(s)-1):
#         skip = 1
#         if s[i-skip] == s[i] or s[i+skip] == s[i]:
#             continue
#         match = s[i-skip]
#         while i-skip>-1 and i+skip<len(s) and s[i-skip]==match and s[i+skip]==match:
#             case_b += 1
#             skip += 1
#     return case_a + case_b


if __name__ == '__main__':
    print(substrCount(int(input()), input()))
