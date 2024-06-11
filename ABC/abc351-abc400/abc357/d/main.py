# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = len(str(n))
    mod = 998244353

    # 等比数列の和
    ans = n * (pow(10, d * n, mod) - 1) * pow(10**d - 1, mod - 2, mod) % mod
    print(ans % mod)


if __name__ == "__main__":
    main()
