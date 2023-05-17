# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil, sqrt

    input = sys.stdin.readline

    r, x, y = map(int, input().split())
    dist = x**2 + y**2

    if r**2 > dist:
        print(2)
    else:
        print(ceil(sqrt(dist) / r))


if __name__ == "__main__":
    main()
