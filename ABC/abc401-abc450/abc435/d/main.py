# -*- coding: utf-8 -*-


def main():
    import sys

    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[bi].append(ai)

    reachable = [False] * n
    q = int(input())

    for _ in range(q):
        query, vi = map(int, input().split())
        vi -= 1

        if query == 1:
            d = deque([vi])

            while d:
                cur = d.popleft()

                if reachable[cur]:
                    continue

                reachable[cur] = True

                for to in graph[cur]:
                    if reachable[to]:
                        continue

                    d.append(to)
        else:
            if reachable[vi]:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
