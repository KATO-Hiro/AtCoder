# -*- coding: utf-8 -*-


def find_cycle(n, edge):
    seen = [False] * n
    finished = [False] * n
    history = []

    for i in range(n):
        if seen[i]:
            continue

        que = [(1, i, -1), (0, i, -1)]
        seen[i] = True

        while que:
            t, vertex, edge_id = que.pop()

            if t == 0:
                if finished[vertex]:
                    continue

                seen[vertex] = True
                history.append((vertex, edge_id))

                for u, id in edge[vertex]:
                    if finished[vertex]:
                        continue

                    if seen[u] and not finished[u]:
                        cycle = [id]

                        while history:
                            vertex, id = history.pop()

                            if vertex == u:
                                break

                            cycle.append(id)

                        return cycle[::-1]

                    elif not seen[u]:
                        que.append((1, u, id))
                        que.append((0, u, id))
            else:
                if finished[vertex]:
                    continue

                history.pop()
                finished[vertex] = True

    return []


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for i, ai in enumerate(a):
        ai -= 1
        graph[i].append((ai, i))

    results = find_cycle(n, graph)

    print(len(results))

    ans = list()

    for result in results:
        ans.append(result + 1)

    # print(results)
    print(*ans)


if __name__ == "__main__":
    main()
