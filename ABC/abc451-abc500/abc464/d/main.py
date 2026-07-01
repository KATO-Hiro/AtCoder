# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    s = input().rstrip()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    inf = 10**18
    dp = [-inf] * 2
    dp[1] = 0

    for i in range(n):
        ndp = [-inf] * 2
        state = s[i] == "S"

        for j in range(2):
            for nj in range(2):
                now = dp[j]

                if nj != state:
                    now -= x[i]
                if j == 0 and nj == 1:
                    now += y[i - 1]

                ndp[nj] = max(ndp[nj], now)

        dp = ndp

    ans = max(dp)
    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
