# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    x = set(map(int, input().split()))
    t1, t2, t3 = map(int, input().split())
    inf = 10**18
    dp = [inf] * (l + 100)
    dp[0] = 0

    for i in range(l):
        # action 1
        add1 = t1

        if i + 1 in x:
            add1 += t3

        dp[i + 1] = min(dp[i + 1], dp[i] + add1)

        # action 2
        add2 = t1 + t2

        if i + 2 in x:
            add2 += t3

        dp[i + 2] = min(dp[i + 2], dp[i] + add2)

        # action 3
        add3 = t1 + t2 * 3

        if i + 4 in x:
            add3 += t3

        dp[i + 4] = min(dp[i + 4], dp[i] + add3)

    ans = dp[l]

    # コーナーケース: ゴールを飛び越えた場合
    if l - 1 >= 0:
        ans = min(ans, dp[l - 1] + (t1 + t2) // 2)
    if l - 2 >= 0:
        ans = min(ans, dp[l - 2] + (t1 + t2) // 2 + t2)
    if l - 3 >= 0:
        ans = min(ans, dp[l - 3] + (t1 + t2) // 2 + t2 * 2)

    print(ans)


if __name__ == "__main__":
    main()
