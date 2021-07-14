# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    g = gcd(a, b)
    g = gcd(g, c)

    print(a // g + b // g + c // g - 3)



if __name__ == "__main__":
    main()
