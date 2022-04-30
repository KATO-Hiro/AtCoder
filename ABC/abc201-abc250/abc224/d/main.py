# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict, deque
    import sys

    input = sys.stdin.readline

    n = 9
    m = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    p = list(map(int, input().split()))
    empty = '8'
    pieces = [empty] * n

    for i, pi in enumerate(p):
        pi -= 1
        pieces[pi] = str(i)
    
    pieces = ''.join(pieces)
    goal = '012345678'
    dist = defaultdict(int)
    dist[pieces] = 0
    q = deque()
    q.append(pieces)

    while q:
        qi = q.popleft()
        di = dist[qi]

        for i in range(n):
            if str(qi[i]) != empty:
                continue

            for to in graph[i]:
                tmp = list(qi)
                tmp[i], tmp[to] = tmp[to], tmp[i]
                tmp = ''.join(tmp)

                if tmp not in dist.keys():
                    dist[tmp] = di + 1
                    q.append(tmp)
    
    if goal not in dist.keys():
        print(-1)
    else:
        print(dist[goal])


if __name__ == "__main__":
    main()
