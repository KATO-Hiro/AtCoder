# -*- coding: utf-8 -*-


def main():
    from math import hypot
    from math import ceil
    import sys

    input = sys.stdin.readline

    r, x, y = map(int, input().split())
    dist = hypot(x, y)

    if dist >= r:
        print(ceil(dist / r))
    else:
        print(2)


if __name__ == "__main__":
    main()
