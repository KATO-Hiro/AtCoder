# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    inf = 10 ** 18
    ans = inf

    for i in range(2):
        if i == 1:
            a = a[::-1]

        dp = [inf] * 2
        dp[0] = 0

        for i in range(n):
            ndp = [inf] * 2

            # 選ばない
            ndp[1] = min(ndp[1], dp[0] + a[i])

            # 選ぶ
            ndp[0] = min(ndp[0], dp[1])
            ndp[1] = min(ndp[1], dp[1] + a[i])

            dp = ndp

        ans = min(ans, min(dp))

    print(ans)


if __name__ == "__main__":
    main()
