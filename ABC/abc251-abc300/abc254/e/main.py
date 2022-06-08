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
    
    q = int(input())
    ans = list()

    # See:
    # https://atcoder.jp/contests/abc254/submissions/32215156
    for i in range(q):
        xi, ki = map(int, input().split())
        xi -= 1

        # BFS
        d = deque()
        d.append((xi, 0))  # vertex, dist
        s = set([xi])  # 集合で頂点を管理

        while d:
            vertex, dist = d.popleft()

            if dist == ki:
                continue

            for to in graph[vertex]:
                if to not in s:
                    s.add(to)
                    d.append((to, dist + 1))
        
        size = len(s)
        ans.append(sum(s) + size)
    
    print(*ans, sep="\n")
        

if __name__ == "__main__":
    main()
