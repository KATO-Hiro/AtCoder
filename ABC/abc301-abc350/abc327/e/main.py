# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate
    from math import sqrt

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    size = 5010
    dp = [0.0] * size
    dp[1] = p[-1]
    r = [0.0] * size
    r[0] = 1.0
    minus = [0.0] * size

    for i in range(1, n + 1):
        r[i] = r[i - 1] * 0.9
        minus[i] = 1200 / sqrt(i)

    r_sum = list(accumulate(r, initial=0))

    for i in range(n - 2, -1, -1):
        ndp = [0.0] * size
        pi = p[i]

        for j in range(n - i + 2):
            ndp[j] = max(ndp[j], dp[j])

            if j + 1 > 5000:
                continue

            ndp[j + 1] = max(ndp[j + 1], dp[j] + r[j] * pi)

        dp = ndp

    ans = list()

    for i in range(1, n + 1):
        candidate = dp[i] / r_sum[i] - minus[i]
        ans.append(candidate)

    print(max(ans))


if __name__ == "__main__":
    main()
