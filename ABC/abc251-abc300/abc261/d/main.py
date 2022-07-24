# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    d = defaultdict(int)

    for i in range(m):
        ci, yi = map(int, input().split())
        d[ci] = yi

    m_max = 5001
    inf = 10 ** 18
    dp = [-inf] * (m_max + 10)
    dp[0] = 0

    # DP
    for i in range(n):
        ndp = [-inf] * (m_max + 10)

        for j in range(m_max):
            # 表
            ndp[j + 1] = max(ndp[j + 1], dp[j] + x[i] + d[j + 1])

            # 裏
            ndp[0] = max(ndp[0], dp[j])

        dp = ndp
    
    ans = 0

    for j in range(n + 1):
        ans = max(ans, dp[j])
    
    print(ans)


if __name__ == "__main__":
    main()
