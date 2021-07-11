# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    used = [False for _ in range(n)]
    dist = [10 ** 7 for _ in range(n)]
    dist[0] = 0
    d = deque()
    d.append(0)

    while d:
        di = d.popleft()
        used[di] = True

        for to in graph[di]:
            if used[to]:
                continue

            dist[to] = min(dist[to], dist[di] + 1)
            d.append(to)
    
    for i in range(q):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1

        if abs(dist[ci] - dist[di]) % 2 == 1:
            print("Road")
        else:
            print("Town")



if __name__ == "__main__":
    main()
