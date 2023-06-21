# -*- coding: utf-8 -*-


def main():
    import sys
    from math import gcd

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c = a * b // gcd(a, b)

    if c > 10**18:
        c = "Large"

    print(c)


if __name__ == "__main__":
    main()
