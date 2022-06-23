# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    sys.setrecursionlimit(10 ** 8)
    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    k_max = 20
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    def merge(original, add):
        result = sorted(original + add, reverse=True)

        if len(result) > k_max:
            result = result[:k_max]
        
        return result
    
    memo = defaultdict(list)
    
    def dfs(cur, parent=-1):
        results = []
        results.append(x[cur])

        for to in graph[cur]:
            if to == parent:
                continue

            values = dfs(to, cur)
            results = merge(results, values)
        
        memo[cur] = results

        return results
    
    dfs(0)

    for i in range(q):
        vi, ki = map(int, input().split())
        vi -= 1
        ki -= 1

        print(memo[vi][ki])


if __name__ == "__main__":
    main()
