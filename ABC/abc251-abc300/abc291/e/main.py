# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    degrees = [0] * n
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[bi].append(ai)
        degrees[ai] += 1
    
    d = deque()

    for i in range(n):
        if degrees[i] == 0:
            d.append(i)

    used, id, ans = [False] * n, n, [0] * n

    while d:
        if len(d) >= 2:
            print("No")
            exit()

        di = d.popleft()

        if used[di]:
            continue

        used[di], ans[di] = True, id
        id -= 1

        for to in graph[di]:
            if used[to]:
                continue

            degrees[to] -= 1

            if degrees[to] == 0:
                d.append(to)
        
    print("Yes")
    print(*ans)


if __name__ == "__main__":
    main()
