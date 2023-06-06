# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    print(n // x * y)


if __name__ == "__main__":
    main()
