# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10 ** 8)
    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]
    ab = list()
    dp = [0] * n
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        ab.append((ai, bi))
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    def dfs(pos, parent=-1):
        dp[pos] = 1

        for v in graph[pos]:
            if v == parent:
                continue

            dfs(v, pos)
            dp[pos] += dp[v]
    
    dfs(0)
    ans = 0

    for ai, bi in ab:
        count = min(dp[ai], dp[bi])
        ans += count * (n - count)
    
    print(ans)


if __name__ == "__main__":
    main()
