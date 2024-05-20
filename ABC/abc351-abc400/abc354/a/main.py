# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h = int(input())
    cur_h = 0
    day = 0

    while cur_h <= h:
        cur_h += 2**day
        day += 1

    print(day)


if __name__ == "__main__":
    main()
