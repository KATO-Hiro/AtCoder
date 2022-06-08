# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
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

    for i in range(q):
        xi, ki = map(int, input().split())
        xi -= 1

        # BFS
        d = deque()
        d.append(xi)
        used = defaultdict(bool)
        dist = defaultdict(int)
        dist[xi] = 0
        summed = xi + 1
        used[xi] = True

        while d:
            di = d.popleft()

            for to in graph[di]:
                if used[to]:
                    continue

                if dist[di] < ki:
                    dist[to] = dist[di] + 1

                    if not used[to]:
                        summed += to + 1

                    used[to] = True
                    d.append(to)
        
        ans.append(summed)
    
    print(*ans, sep="\n")
        

if __name__ == "__main__":
    main()
