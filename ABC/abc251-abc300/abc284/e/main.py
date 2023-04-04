# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    visited = [False] * n
    upper, ans = 10 ** 6, 0
    d = deque()
    d.append((0, -1)) # node, parent

    while d:
        cur, parent = d.pop()
        
        if cur >= 0:
            visited[cur] = True
            d.append((~cur, parent))

            for to in graph[cur]:
                if to == parent or visited[to]:
                    continue

                d.append((to, cur))
        else:
            cur = ~cur
            visited[cur] = False
            ans += 1

            if ans >= upper:
                break
    
    print(ans)


if __name__ == "__main__":
    main()
