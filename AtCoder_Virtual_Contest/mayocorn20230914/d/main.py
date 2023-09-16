# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    d = defaultdict(int)

    for _ in range(m):
        ci, yi = map(int, input().split())
        d[ci] = max(d[ci], yi)

    pending = -1
    dp = [pending] * (n + 1)
    dp[0] = 0

    for i, xi in enumerate(x):
        ndp = [pending] * (n + 1)

        for j in range(n + 1):
            if dp[j] == pending:
                continue

            ndp[0] = max(ndp[0], dp[j])
            nj = j + 1

            if nj > n:
                continue

            ndp[nj] = max(ndp[nj], dp[j] + xi + d[nj])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
