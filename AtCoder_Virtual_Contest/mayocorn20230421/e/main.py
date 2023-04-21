# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict, deque
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi, wi = map(int, input().split())
        ai -= 1
        bi -= 1
        wi %= 2  # 偶奇のみ関心
    
        graph[ai].append((wi, bi))
        graph[bi].append((wi, ai))
    
    q = deque()
    q.append((0, 0))  # dist % 2, vertex
    visited = [False] * n
    inf = 10 ** 18
    d = [inf] * n
    d[0] = 0
    ans = [0] * n
    ans[0] = 0

    while q:
        dist, cur = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for delta, to in graph[cur]:
            next_dist = (dist + delta) % 2

            if dist % 2 == next_dist:
                ans[to] = ans[cur]
            else:
                ans[to] = 1 - ans[cur]
            
            q.append((next_dist, to))

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
