# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d, e, f = map(int, input().split())
    mod = 998244353
    ans = 1

    ans = a * b
    ans *= c
    ans %= mod
    
    ans2 = 1
    ans2 = d * e
    ans2 %= mod
    ans2 *= f
    ans2 %= mod

    print((ans - ans2) % mod)


if __name__ == "__main__":
    main()
