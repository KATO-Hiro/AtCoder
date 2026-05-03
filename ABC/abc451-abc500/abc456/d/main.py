# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    s = input().rstrip()
    dp = defaultdict(int)
    mod = 998244353

    for si in s:
        dp[si] = dp["a"] + dp["b"] + dp["c"] + 1
        dp[si] %= mod

    ans = sum(dp.values()) % mod
    print(ans)


if __name__ == "__main__":
    main()
