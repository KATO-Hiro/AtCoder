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
    
    d = deque()
    d.append(0)
    inf = float("inf")
    ages = [inf] * n
    ages[0] = 0

    while d:
        di = d.popleft()

        for to in graph[di]:
            if ages[to] != inf:
                continue

            ages[to] = ages[di] + 1
            d.append(to)
    
    for age in ages:
        print(min(age, 120))


if __name__ == "__main__":
    main()
