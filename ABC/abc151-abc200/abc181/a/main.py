# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n % 2 == 0:
        print('White')
    else:
        print('Black')


if __name__ == "__main__":
    main()
