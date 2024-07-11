# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = input().rstrip()
    b = input().rstrip()
    small, large = list(), list()

    for ai, bi in zip(a, b):
        if ai > bi:
            small.append(bi)
            large.append(ai)
        else:
            small.append(ai)
            large.append(bi)

    mod = 998244353
    d1, d2 = 1, 1
    a2, b2 = 0, 0

    for si in small[::-1]:
        a2 += d1 * int(si) % mod
        d1 *= 10
        d1 %= mod

    for lj in large[::-1]:
        b2 += d2 * int(lj) % mod
        d2 *= 10
        d2 %= mod

    ans = a2 * b2 % mod
    print(ans)


if __name__ == "__main__":
    main()
