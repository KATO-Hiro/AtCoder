# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(accumulate(a))
    mod = 998244353
    ans = 0

    for i in range(1, n):
        ai = a[i]
        digit = len(list(str(ai)))
        ans += b[i - 1] * pow(10, digit, mod)
        ans %= mod
        ans += ai * i
        ans %= mod

    print(ans % mod)


if __name__ == "__main__":
    main()
