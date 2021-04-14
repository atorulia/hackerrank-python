import re


if __name__ == '__main__':
    string = input()
    substring = input()

    matches = re.finditer(fr"(?=({substring}))", string)
    is_match = False

    for match in matches:
        is_match = True
        print(f"({match.start(1)}, {match.end(1) - 1})")

    if not is_match:
        print("(-1, -1)")





