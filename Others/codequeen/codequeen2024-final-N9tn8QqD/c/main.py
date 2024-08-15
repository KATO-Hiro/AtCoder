# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k, t = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(accumulate(p, initial=0))
    inf = 10**18
    dp = [0] * (n + 10)

    for _ in range(k):
        ndp = [inf] * (n + 10)

        # 貰うDP
        for i in range(t, n + 1):
            if dp[i - t] == inf:
                continue

            ndp[i] = min(ndp[i], dp[i - t] + q[i] - q[i - t])
            # 直前の降車時刻の結果と比較
            ndp[i] = min(ndp[i], ndp[i - 1])

        dp = ndp

    print(min(dp[: n + 1]))


if __name__ == "__main__":
    main()
