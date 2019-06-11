# -*- coding: utf-8 -*-


def main():
    import sys

    n = int(input())

    for line in sys.stdin.readlines():
        ai, bi = map(int, line.split())
        print(ai * bi)


if __name__ == '__main__':
    main()
