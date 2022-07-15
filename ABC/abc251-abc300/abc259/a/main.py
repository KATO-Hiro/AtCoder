# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, x, t, d = map(int, input().split())

    if x <= m <= n:
        print(t)
    else:
        print(t - (x - m) * d)


if __name__ == "__main__":
    main()
