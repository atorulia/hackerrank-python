from functools import cmp_to_key


class Player:
    """
    Declare a Checker class that implements the comparator method as described. It should sort first descending by
    score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method
    to sort the data, and prints it out properly.
    """
    def __init__(self, _name: str, _score: int):
        """
        :param _name: a string
        :param _score: an integer
        """
        self.name = _name
        self.score = _score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a, b):
        if a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1
        else:
            return b.score - a.score


if __name__ == '__main__':
    n = int(input())
    data = []

    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
