# -*- coding: utf-8 -*-


def main():
    import sys
    sys.setrecursionlimit(10 ** 8)

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    ans = list()
    
    def dfs(cur, parent=-1):
        if cur == y:
            ans.append(cur + 1)
            print(*ans)
            exit()

        for to in graph[cur]:
            if to == parent:
                continue

            ans.append(cur + 1)
            dfs(to, cur)
            ans.pop()
    
    dfs(x)


if __name__ == "__main__":
    main()
