# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n, m, k, s, t, x = map(int, input().split())
    s -= 1
    t -= 1
    x -= 1
    edges = list()
    mod = 998244353
    
    for _ in range(m):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1
    
        edges.append((ui, vi))
    
    dp = [[0] * 2 for _ in range(n)] 
    dp[s][0] = 1

    for i in range(k):
        ndp = [[0] * 2 for _ in range(n)] 

        for ui, vi in edges:
            for c in range(2):
                ndp[vi][c] += dp[ui][c ^ (vi == x)]

                if ndp[vi][c] >= mod:
                    ndp[vi][c] -= mod

                ndp[ui][c] += dp[vi][c ^ (ui == x)]

                if ndp[ui][c] >= mod:
                    ndp[ui][c] -= mod

        dp = ndp

    print(dp[t][0])


if __name__ == "__main__":
    main()
