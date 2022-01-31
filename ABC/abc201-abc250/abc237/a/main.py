# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    number_max = 2 ** 31

    if - number_max <= n < number_max:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
