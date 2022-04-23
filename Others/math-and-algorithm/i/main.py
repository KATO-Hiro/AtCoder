# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (s + 10)
    dp[0] = True

    for i in range(n):
        ndp = [False] * (s + 10)
        ai = a[i]

        for j in range(s + 1):
            if not dp[j]:
                continue

            ndp[j] = dp[j]

            if j + ai <= s:
                ndp[j + ai] = dp[j]

        dp = ndp

    if dp[s]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
