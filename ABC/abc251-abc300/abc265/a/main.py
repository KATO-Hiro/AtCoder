# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, n = map(int, input().split())

    print(min(x * n, n // 3 * y + (n % 3) * x))


if __name__ == "__main__":
    main()
