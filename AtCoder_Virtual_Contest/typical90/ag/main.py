# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    h, w = map(int, input().split())

    if h == 1 or w == 1:
        print(h * w)
    else:
        print(ceil(h / 2) * ceil(w / 2))


if __name__ == "__main__":
    main()
