# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    mod = 998244353
    ans = 1

    ans *= a * (a + 1) // 2
    ans %= mod
    ans *= b * (b + 1) // 2
    ans %= mod
    ans *= c * (c + 1) // 2
    ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
