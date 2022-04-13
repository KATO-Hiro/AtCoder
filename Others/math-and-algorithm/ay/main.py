# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n %= 4

    if n == 0:
        print(6)
    elif n == 1:
        print(2)
    elif n == 2:
        print(4)
    else:
        print(8)


if __name__ == "__main__":
    main()
