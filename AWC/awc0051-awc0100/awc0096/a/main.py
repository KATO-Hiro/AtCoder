# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    s = [0] * n
    s[0] = ab[0][0]

    for i in range(n - 1):
        _, bi = ab[i]
        aj, _ = ab[i + 1]
        s[i + 1] = max(s[i] + bi, aj)

    print(s[-1] + ab[-1][1])


if __name__ == "__main__":
    main()
