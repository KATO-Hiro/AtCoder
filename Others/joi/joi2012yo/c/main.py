# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b = map(int, input().split())
    c = int(input())
    pending = -1
    size = 10**5 + 2 * 10**3
    dp = [pending] * size
    dp[a] = c
    ans = 0

    # DP
    for i in range(n):
        di = int(input())
        ndp = [pending] * size

        for j in range(a, size):
            if dp[j] == pending:
                continue

            ndp[j] = max(ndp[j], dp[j])
            ndp[j + b] = max(ndp[j + b], dp[j] + di)

        dp = ndp

        for j in range(a, size):
            ans = max(ans, dp[j] // j)

    print(ans)


if __name__ == "__main__":
    main()
