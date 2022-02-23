# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    h = int(input())
    print(sqrt(h * (12800000 + h)))


if __name__ == "__main__":
    main()
