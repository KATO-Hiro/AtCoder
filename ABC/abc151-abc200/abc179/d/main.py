# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 998244353
    left = [0 for _ in range(k)]
    right = [0 for _ in range(k)]
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    summed = [0 for _ in range(n + 1)]
    summed[1] = 1

    for i in range(k):
        li, ri = map(int, input().split())

        left[i] = li
        right[i] = ri

    for i in range(2, n + 1):
        for l, r in zip(left, right):
            ri = i - l
            li = max(i - r, 1)

            if ri < 0:
                continue

            dp[i] += summed[ri] - summed[li - 1]
            dp[i] %= mod

        summed[i] = summed[i - 1] + dp[i]
        summed[i] %= mod

    print(dp[n])


if __name__ == "__main__":
    main()
