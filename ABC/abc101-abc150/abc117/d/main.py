# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # See:
    # https://drken1215.hatenablog.com/entry/2019/02/04/013700
    # dp[digit][is_smaller]
    dp = [[-1 for _ in range(100)] for _ in range(2)]
    dp[0][0] = 0
    digit_max = 50

    for digit in range(digit_max):
        mask = 1 << (digit_max - digit - 1)
        count = 0

        for ai in a:
            if ai & mask:
                count += 1

        cost0 = mask * count
        cost1 = mask * (n - count)

        # smaller to smaller
        if dp[1][digit] != -1:
            dp[1][digit + 1] = max(dp[1][digit + 1], dp[1][digit] + max(cost0, cost1))

        # exact to smaller
        if dp[0][digit] != -1 and (k & mask):
            dp[1][digit + 1] = max(dp[1][digit + 1], dp[0][digit] + cost0)

        # exact to exact
        if dp[0][digit] != -1:
            if k & mask:
                dp[0][digit + 1] = max(dp[0][digit + 1], dp[0][digit] + cost1)
            else:
                dp[0][digit + 1] = max(dp[0][digit + 1], dp[0][digit] + cost0)

    print(max(dp[0][digit_max], dp[1][digit_max]))


if __name__ == "__main__":
    main()
