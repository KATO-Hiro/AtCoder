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

    mod = 998244353
    dp = [0] * n
    dp[0] = 1

    for _ in range(k):
        total = sum(dp) % mod
        ndp = [total] * n

        for u, v in graph:
            ndp[u] -= dp[v]
            ndp[v] -= dp[u]

        for i in range(n):
            ndp[i] -= dp[i] 
            ndp[i] %= mod
        
        dp = ndp

    print(dp[0] % mod)


if __name__ == "__main__":
    main()
