# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 8)

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    # See:
    # https://qiita.com/drken/items/a803d4fc4a727e02f7ba#4-3-%E4%BA%8C%E9%83%A8%E3%82%B0%E3%83%A9%E3%83%95%E5%88%A4%E5%AE%9A
    colors = [-1] * n  # 訪問済みかどうかのフラグも兼ねている
    is_bipartite = True

    def dfs(v:int, cur:int=0) -> bool:
        colors[v] = cur

        for to in graph[v]:
            if colors[to] != -1:
                # 同じ色はNG
                if colors[to] == cur:
                    return False

                continue

            # 1回でもNGだったら、二部グラフではない
            if not dfs(to, 1 - cur):
                return False
        
        return True
    
    for v in range(n):
        if colors[v] != -1:
            continue

        if not dfs(v):
            is_bipartite = False
    
    if is_bipartite:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
