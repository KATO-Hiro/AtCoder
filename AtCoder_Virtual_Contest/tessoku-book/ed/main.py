# -*- coding: utf-8 -*-


def digit_sum(n: int) -> int:
    summed = 0

    while n > 0:
        summed += n % 10
        n //= 10

    return summed


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    dp = [[0 for _ in range(n + 1)] for _ in range(30)]

    for i in range(n + 1):
        dp[0][i] = i - digit_sum(i)

    for d in range(1, 30):
        for i in range(n + 1):
            dp[d][i] = dp[d - 1][dp[d - 1][i]]

    for i in range(1, n + 1):
        k2 = k
        value = i
        d = 0

        while k2 > 0:
            if k2 & 1:
                value = dp[d][value]

            k2 >>= 1
            d += 1

        print(value)


if __name__ == "__main__":
    main()
