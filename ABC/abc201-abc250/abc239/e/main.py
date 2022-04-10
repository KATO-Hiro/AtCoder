# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10 ** 8)
    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    k = 20
    values = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    def merge(a, b):
        c = sorted(a + b, reverse=True)

        if len(c) > k:
            c = c[:k]
        
        return c
    
    def dfs(cur, parent=-1):
        results = [x[cur]]

        for to in graph[cur]:
            if to == parent:
                continue

            d = dfs(to, cur)
            results = merge(results, d)
        
        values[cur] = results
        return results

    dfs(0)
    
    for i in range(q):
        vi, ki = map(int, input().split())
        vi -= 1
        ki -= 1

        ans = values[vi][ki]
        print(ans)


if __name__ == "__main__":
    main()
