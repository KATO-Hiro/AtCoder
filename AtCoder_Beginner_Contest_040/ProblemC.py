'''input
4
100 125 80 110
40

9
314 159 265 358 979 323 846 264 338
310

4
100 150 130 120
40

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # i = n
    i = 1
    dp = [0] * n
    cost = 0

    for i in range(2, n):
        candidate1 = dp[i - 2] + abs(a[i - 2] - a[i])
        candidate2 = dp[i - 1] + abs(a[i - 1] - a[i])
        dp[i] = min(candidate1, candidate2)

    # print(sum(dp))
    # print(dp[n])

    # while i > 0:
    #     if i == 1:
    #         # cost += abs(a[i + 1] - a[i])
    #         cost += abs(a[i] - a[i - 1])
    #         # i += 1
    #         i -= 1
    #     else:
    #         # candidate1 = abs(a[i + 1] - a[i])
    #         # candidate2 = abs(a[i + 2] - a[i])
    #         candidate1 = abs(a[i] - a[i - 1])
    #         candidate2 = abs(a[i] - a[i - 2])

    #         if candidate1 > candidate2:
    #             cost += candidate2
    #             # i += 2
    #             i -= 2
    #         else:
    #             cost += candidate1
    #             # i += 1
    #             i -= 1

    # print(cost)
