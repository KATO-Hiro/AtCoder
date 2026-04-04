# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    scores = []
    inf = 10**18

    for i, ai in enumerate(a, 1):
        score = 0

        for j, aij in enumerate(ai, 1):
            score += inf * aij * (2 ** (j - 1))

        scores.append((score - i, i))

    scores.sort(key=lambda x: (-x[0], x[1]))

    for i in range(4):
        print(scores[i][1])


if __name__ == "__main__":
    main()
