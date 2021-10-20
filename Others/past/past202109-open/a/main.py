# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())

    print(min(a + b - c, d))


if __name__ == "__main__":
    main()
