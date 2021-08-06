# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    graph = []
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph.append((ai, bi))
    
    dp = [0] * n
    dp[0] = 1
    mod = 998244353

    for _ in range(k):
        summed = sum(dp) % mod
        ndp = [summed] * n

        for i in range(n):
            ndp[i] -= dp[i]
            ndp[i] %= mod

        for ui, vi in graph:
            ndp[ui] -= dp[vi]
            ndp[ui] %= mod
            ndp[vi] -= dp[ui]
            ndp[vi] %= mod
        
        dp = ndp
    
    print(dp[0])


if __name__ == "__main__":
    main()
