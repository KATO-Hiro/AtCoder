# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k, s, t, x = map(int, input().split())    
    s -= 1
    t -= 1
    x -= 1

    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    dp = [[0] * 2 for _ in range(n + 10)]  # 頂点v、整数xの登場回数mod 2
    dp[s][0] = 1
    mod = 998244353

    # See:
    # https://www.youtube.com/watch?v=CEUTTd1gHxU
    for _ in range(k):
        ndp = [[0] * 2 for _ in range(n + 10)]

        for v in range(n):
            for i in range(2):
                for to in graph[v]:
                    nv = to
                    ni = i 

                    if to == x:
                        ni ^= 1

                    ndp[nv][ni] += dp[v][i]

                    if ndp[nv][ni] >= mod:
                        ndp[nv][ni] -= mod

        dp = ndp
    
    print(dp[t][0])


if __name__ == "__main__":
    main()
