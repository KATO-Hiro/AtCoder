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
        d[ci] = yi

    dp = [0] * (n + 1)

    for i, xi in enumerate(x):
        ndp = [0] * (n + 1)

        for j in range(i + 1):
            ndp[0] = max(ndp[0], dp[j])

            if j + 1 > n:
                continue

            value = dp[j] + xi

            if (j + 1) in d.keys():
                value += d[j + 1]

            ndp[j + 1] = max(ndp[j + 1], value)

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
