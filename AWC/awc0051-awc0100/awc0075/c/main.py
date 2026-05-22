# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, t = map(int, input().split())
    s -= t
    inf = 10**18
    dp = [-inf] * (s + 1)
    dp[-1] = 0

    for i in range(n):
        ci, vi = map(int, input().split())
        ndp = [-inf] * (s + 1)

        for j in range(s, -1, -1):
            if dp[j] == -inf:
                continue

            ndp[j] = max(ndp[j], dp[j])
            nj = j - ci

            if nj < 0:
                continue

            ndp[nj] = max(ndp[nj], dp[j] + vi)

        dp = ndp

    ans = max(dp)
    print(ans)


if __name__ == "__main__":
    main()
