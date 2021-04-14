import re


def detect_floating_point_number(string: str) -> bool:
    return bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', string))


if __name__ == '__main__':
    for _ in range(int(input())):
        print(detect_floating_point_number(input()))
