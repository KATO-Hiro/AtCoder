# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    mod = 10 ** 9 + 7
    broken = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 2)]
    dp[n] = 1

    for i in range(m):
        ai = int(input())
        broken[ai] = True

    # See:
    # https://www.youtube.com/watch?v=L8grWxBlIZ4
    for j in range(n - 1, -1, -1):
        if broken[j]:
            continue

        dp[j] = dp[j + 1] + dp[j + 2]
        dp[j] %= mod

    print(dp[0])


if __name__ == '__main__':
    main()
