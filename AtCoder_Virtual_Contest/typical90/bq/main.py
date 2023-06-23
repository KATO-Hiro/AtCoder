# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = k

    if n >= 2:
        ans *= (k - 1) * pow(max(0, k - 2), n - 2, mod) % mod

    print(ans % mod)


if __name__ == "__main__":
    main()
