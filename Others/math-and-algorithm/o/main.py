# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
