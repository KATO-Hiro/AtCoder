# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]

    for i in range(q):
        si = list(map(int, input().split()))
        a = si[1] - 1

        if si[0] == 1:
            b = si[2] - 1
            graph[a].append(b)
        elif si[0] == 2:

            for j in range(n):
                if j == a:
                    continue

                if a in graph[j]:
                    graph[a].append(j)
        else:
            d = deque(graph[a])

            while d:
                c = d.popleft()

                for di in graph[c]:
                    if di == a:
                        continue

                    if not di in graph[a]:
                        graph[a].append(di)

    ans = [['N' for _ in range(n)] for _ in range(n)]

    for index, g in enumerate(graph):
        for gi in g:
            ans[index][gi] = 'Y'

    for i in range(n):
        print(''.join(map(str, ans[i])))


if __name__ == '__main__':
    main()
