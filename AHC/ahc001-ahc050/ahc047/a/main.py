# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, l = map(int, input().split())
    sp = [tuple(map(str, input().split())) for _ in range(n)]

    for _ in range(m):
        a = [100] + [0] * (m - 1)
        print("a", *a)


if __name__ == "__main__":
    main()
