# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a = int(input())

    print(a + (a ** 2) + (a ** 3))


if __name__ == '__main__':
    main()
