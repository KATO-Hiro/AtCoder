# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input()
    digit = len(s)
    n = int(s)
    mod = 998244353 
    ans = 0
    minus = 0

    for d in range(1, digit):
        m = min(10 ** d - 1, n)
        k = m - minus

        ans += k * (k + 1) // 2
        ans %= mod

        minus = m

    print(ans)


if __name__ == "__main__":
    main()
