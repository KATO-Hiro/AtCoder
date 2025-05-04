# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 豆が入っているときに、まとめて操作
    n = int(input())
    c = [0] + list(map(int, input().split()))
    a = [1] + list(map(int, input().split()))

    # 豆が入っている茶碗ごとに、操作回数の最小値（最短路問題）を解く
    nc = list()
    inf = 10**9
    ans = 0

    def solve(array):
        m = len(array)
        dp = [inf] * (m + 1)
        dp[0] = 0

        for i in range(m):
            now = inf

            for j in range(array[i]):
                if i - j < 0:
                    break

                now = min(now, dp[i - j])

            dp[i + 1] = min(dp[i + 1], now + 1)

        return dp[m]

    for i in range(1, n):
        nc.append(c[i])

        if a[i] == 0:
            continue

        ans += solve(nc)
        nc = list()

    print(ans)


if __name__ == "__main__":
    main()
