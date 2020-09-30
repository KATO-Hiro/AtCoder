# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())

    if (d < a) or (c > b):
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
