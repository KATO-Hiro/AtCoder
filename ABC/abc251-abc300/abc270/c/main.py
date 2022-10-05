# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

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
    
    d = deque()
    d.append(y)
    not_used = -1
    pos = [not_used] * n

    while d:
        cur = d.popleft()

        for to in graph[cur]:
            if pos[to] == not_used:
                pos[to] = cur
                d.append(to)

    now = x
    ans = list()

    while now != y:
        ans.append(now + 1)
        now = pos[now]
    
    ans.append(y + 1)
    
    print(*ans)


if __name__ == "__main__":
    main()
