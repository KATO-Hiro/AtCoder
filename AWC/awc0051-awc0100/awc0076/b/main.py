# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    scores = []

    for i in range(n):
        ai, bi = map(int, input().split())
        scores.append((bi, ai, i + 1))

    scores = sorted(scores, key=lambda x: (-x[0], -x[1], x[2]))

    for _, _, i in scores:
        print(i)


if __name__ == "__main__":
    main()
