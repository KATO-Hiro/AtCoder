# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    inf = 10**9
    b = list(map(int, input().split()))
    dp = [inf] * n
    dp[0] = 0
    memo = [-1] * n

    for i in range(1, n):
        dp[i] = min(dp[i], dp[i - 1] + a[i - 1])
        memo[i] = i - 1

        if i >= 2:
            tmp = dp[i - 2] + b[i - 2]

            if dp[i] > tmp:
                dp[i] = tmp
                memo[i] = i - 2

    pos = n - 1
    ans = list()

    while memo[pos] != -1:
        ans.append(pos + 1)
        pos = memo[pos]

    print(len(ans) + 1)
    print(1, *ans[::-1])


if __name__ == "__main__":
    main()
