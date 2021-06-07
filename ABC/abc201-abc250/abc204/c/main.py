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

    ans = 0

    for i in range(n):
        visited = [False for _ in range(n)]
        visited[i] = True
        d = deque()
        d.append(i)
        count = 1

        while d:
            di = d.pop()

            for to in graph[di]:
                if visited[to]:
                    continue

                visited[to] = True
                count += 1
                d.append(to)

        ans += count

    print(ans)


if __name__ == "__main__":
    main()
