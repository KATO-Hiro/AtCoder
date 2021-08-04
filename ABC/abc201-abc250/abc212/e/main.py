# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)

    mod = 998244353
    dp = [0 for _ in range(n)]
    dp[0] = 1

    for ki in range(k):
        next_dp = [0 for _ in range(n)]
        dp, next_dp = next_dp, dp # swap

        total = sum(next_dp)
        total %= mod

        for i in range(n):
            dp[i] = total

            for to in graph[i]:
                dp[i] -= next_dp[to]
            
            dp[i] -= next_dp[i] # self
            dp[i] %= mod

    print(dp[0])


if __name__ == "__main__":
    main()
