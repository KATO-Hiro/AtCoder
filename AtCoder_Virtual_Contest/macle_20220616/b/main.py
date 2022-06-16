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
    
    used = [False] * n
    ans = list()

    def dfs(cur, parent=-1):
        used[cur] = True

        for to in sorted(graph[cur]):
            if used[to]:
                continue

            ans.append(cur + 1)
            dfs(to, cur)
            ans.append(to + 1)
    
    dfs(0)
    ans.append(1)
    print(*ans)

if __name__ == "__main__":
    main()
