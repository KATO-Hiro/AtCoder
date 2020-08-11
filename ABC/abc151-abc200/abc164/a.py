# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    s, w = map(int, input().split())

    if s <= w:
        print('unsafe')
    else:
        print('safe')


if __name__ == '__main__':
    main()
