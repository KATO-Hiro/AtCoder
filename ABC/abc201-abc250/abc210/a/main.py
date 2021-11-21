# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, x, y = map(int, input().split())

    print(min(a, n) * x + max(0, n - a) * y)


if __name__ == "__main__":
    main()
