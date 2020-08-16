# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = [float(input()) for _ in range(n)]

    from itertools import combinations

    for x, y in list(combinations(a, 2)):
        if (x * y).is_integer():
            print(x, y, x * y)


if __name__ == '__main__':
    main()
