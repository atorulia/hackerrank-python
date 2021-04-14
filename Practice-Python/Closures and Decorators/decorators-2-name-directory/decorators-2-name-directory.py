def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda item: int(item[2])))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    print(*name_format([input().split() for i in range(int(input()))]), sep='\n')
