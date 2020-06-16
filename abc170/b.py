# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x, y = map(int, input().split())

    crane = (4 * x) - y
    turtle = y - (2 * x)

    if crane >= 0 and turtle >= 0 and crane % 2 == 0 and turtle % 2 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
