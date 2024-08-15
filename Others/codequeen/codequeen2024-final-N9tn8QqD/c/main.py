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
        candidate = inf

        for i in range(n + 1):
            j = i + t

            if dp[i] == inf:
                continue
            if j > n:
                break

            candidate = min(candidate, dp[i] + q[j] - q[i])
            ndp[j] = min(ndp[j], candidate)

        dp = ndp

    print(min(dp[: n + 1]))


if __name__ == "__main__":
    main()
