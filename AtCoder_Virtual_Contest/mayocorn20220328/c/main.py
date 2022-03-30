# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    print(k * (k - 1) ** (n - 1))


if __name__ == "__main__":
    main()
