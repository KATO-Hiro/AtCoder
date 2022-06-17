# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10 ** 8)
    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    ans = list()

    def dfs(cur, parent=-1):
        ans.append(cur + 1)

        for to in sorted(graph[cur]):
            if to == parent:
                continue

            dfs(to, cur)
            ans.append(cur + 1)
    
    dfs(0)
    print(*ans)

if __name__ == "__main__":
    main()
