# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list(input())
    t = list("atcoder")
    m = len(t)
    mod = 10 ** 9 + 7
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1

    for si in s:
        for j in range(m):
            if si == t[j]:
                dp[j + 1] += dp[j]
                dp[j + 1] %= mod

    print(dp[m])


if __name__ == "__main__":
    main()
