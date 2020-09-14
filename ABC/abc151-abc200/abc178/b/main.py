# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())

    print(max(a * d, b * c, a * c, b * d))


if __name__ == '__main__':
    main()
