# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d, e, f = map(int, input().split())
    mod = 998244353
    ans = (a * b * c - d * e * f) % mod
    print(ans)


if __name__ == "__main__":
    main()
