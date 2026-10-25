# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if (a + b) >= 10:
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()
