# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 998244353

    ans = n * (n + 1) // 2
    ans %= mod
    b = 1

    while b <= n:
        y = n // b
        nb = n // y + 1

        ans -= y * (nb - b)
        ans %= mod

        b = nb

    print(ans)


if __name__ == "__main__":
    main()
