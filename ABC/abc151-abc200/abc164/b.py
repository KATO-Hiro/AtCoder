# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())

    while True:
        c -= b

        if c <= 0:
            print('Yes')
            exit()

        a -= d

        if a <= 0:
            print('No')
            exit()


if __name__ == '__main__':
    main()
