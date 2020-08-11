# -*- coding: utf-8 -*-
# AtCoder Beginner Contest
# Problem C


if __name__ == '__main__':
    n = int(input())
    dp = [0] + [100001 for _ in range(n + 1)]

    # See:
    # https://www.youtube.com/watch?v=I-8BnRkq6Ow
    for i in range(1, n + 1):
        power = 1

        while power <= i:
            dp[i] = min(dp[i], dp[i - power] + 1)
            power *= 6

        power = 1

        while power <= i:
            dp[i] = min(dp[i], dp[i - power] + 1)
            power *= 9

    print(dp[n])
