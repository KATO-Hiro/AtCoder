# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    w = list(map(int, input().split()))

    for _ in range(m):
        _, *ai = map(int, input().split())
        total = 0

        for aij in ai:
            aij -= 1
            total += w[aij]

        print(total)


if __name__ == "__main__":
    main()
