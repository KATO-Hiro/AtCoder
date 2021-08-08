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
    
    visited = [False] * n
    ans = list()
    
    def dfs(cur, prev=-1):
        visited[cur] = True
        ans.append(cur + 1)

        for to in sorted(graph[cur]):
            if visited[to]:
                continue

            dfs(to, cur)


        if cur == 0:
            return
        else:
            ans.append(prev + 1)

    
    dfs(0)
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main()
