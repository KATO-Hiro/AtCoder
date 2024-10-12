# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    digit = 60  #  k = 10 ** 18 < 2 ** 60
    dp = [[0 for _ in range(n + 1)] for _ in range(digit)]

    # Doubling
    for i in range(1, n + 1):
        dp[0][i] = x[i - 1]  # TODO: Update value.

    for d in range(1, digit):
        for j in range(n + 1):
            dp[d][j] = dp[d - 1][dp[d - 1][j]]

    ans = list()

    # Find the result of the k-th operation.
    for j in range(1, n + 1):
        u = j

        for di in range(digit):
            if (k >> di) & 1:
                u = dp[di][u]

        ans.append(a[u - 1])

    print(*ans)


if __name__ == "__main__":
    main()
