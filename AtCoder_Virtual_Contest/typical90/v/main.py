# -*- coding: utf-8 -*-


def main():
    import sys
    from math import gcd

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    g = gcd(gcd(a, b), c)
    ans = a // g - 1
    ans += b // g - 1
    ans += c // g - 1
    print(ans)


if __name__ == "__main__":
    main()
