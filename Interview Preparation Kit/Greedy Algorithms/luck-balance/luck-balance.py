def luckBalance(k, contests):
    pass


if __name__ == '__main__':
    nk = input().split()

    print(luckBalance(k=int(nk[1]), contests=[list(map(int, input().rstrip().split())) for _ in range(int(nk[0]))]))
