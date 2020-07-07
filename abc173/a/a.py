# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    n %= 1000

    if n == 0:
        print(0)
    else:
        print(1000 - n)


if __name__ == '__main__':
    main()
