# -*- coding: utf-8 -*-


def main():
    import sys
    from math import gcd

    input = sys.stdin.readline

    n, x = map(int, input().split())
    y = list(map(int, input().split())) + [x]
    y = sorted(y)
    diff = list()

    for y1, y2 in zip(y, y[1:]):
        diff.append(y2 - y1)

    print(gcd(*diff))


if __name__ == "__main__":
    main()
