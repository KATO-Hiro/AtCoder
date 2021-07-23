# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
    ab = sorted([tuple(map(int, input().split())) for _ in range(n)])
    ans = 0

    for i in range(n):
        for ti in range(t):
            dp[i + 1][ti] = max(dp[i + 1][ti], dp[i][ti])
            ai, bi = ab[i]

            if ti + ai < t:
                dp[i + 1][ti + ai] = max(dp[i + 1][ti + ai], dp[i][ti] + bi)
        
        now = dp[i][t - 1] + bi
        ans = max(ans, now)
    
    print(ans)



if __name__ == "__main__":
    main()
