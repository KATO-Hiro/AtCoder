# -*- coding: utf-8 -*-

mod = 10**9 + 7


def f(n):
    return n * (n + 1) // 2


def calc(n):
    prev = 0
    ans = 0

    for d in range(1, 20):
        lower = 10 ** (d - 1)
        upper = min(n, 10**d - 1)

        if lower > upper:
            break

        ans += (f(upper) - prev) * d
        ans %= mod
        prev = f(upper)

    return ans


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())
    print((calc(r) - calc(l - 1)) % mod)


if __name__ == "__main__":
    main()
