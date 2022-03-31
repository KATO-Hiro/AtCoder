# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # bi: edge (0-indexed)
        edges[ai].append(bi)
        edges[bi].append(ai)
    
    d = deque()
    d.append(0)
    visited = [False for _ in range(n)]
    ans = [float("inf") for _ in range(n)]
    ans[0] = 0

    while d:
        di = d.popleft()

        for to in edges[di]:
            if visited[to]:
                continue
            
            ans[to] = di + 1
            visited[to] = True
            d.append(to)
    
    print("Yes")
    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
