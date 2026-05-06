# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    mod = 10**9 + 7
    ans = sum(s[:-1])
    ans %= mod
    ans += s[-1] * pow(2, k, mod)
    ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
