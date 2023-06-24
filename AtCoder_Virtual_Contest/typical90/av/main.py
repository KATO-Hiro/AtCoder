# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    score = list()

    for _ in range(n):
        ai, bi = map(int, input().split())
        score.append(bi)
        score.append(ai - bi)

    print(sum(sorted(score, reverse=True)[:k]))


if __name__ == "__main__":
    main()
