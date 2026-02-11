# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    if x <= 0:
        print("12:{:02d}".format(x * -1))
    else:
        print("11:{:02d}".format(60 - x))


if __name__ == "__main__":
    main()
