# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    print(21 - (a + b + c))


if __name__ == "__main__":
    main()
