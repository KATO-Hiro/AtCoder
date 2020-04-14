# -*- coding: utf-8 -*-


def main():
    from math import pi
    import sys
    input = sys.stdin.readline

    oa, ab, bc = map(int, input().split())
    len_max = (oa + ab + bc)
    diff = oa - (ab + bc)

    if diff > 0:
        len_min = diff
    else:
        len_min = 0

    len_min = 9

    print(((len_max ** 2) - (len_min ** 2)) * pi)


if __name__ == '__main__':
    main()
