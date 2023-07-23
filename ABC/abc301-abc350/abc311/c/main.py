# -*- coding: utf-8 -*-


def find_cycle(n, edge):
    seen = [0] * n
    finished = [0] * n
    stc = []
    for i in range(n):
        if seen[i]:
            continue
        todo = [(1, i, -1), (0, i, -1)]
        seen[i] = True
        while todo:
            t, v, edge_id = todo.pop()
            if t == 0:
                if finished[v]:
                    continue
                seen[v] = 1
                stc.append((v, edge_id))
                for u, id in edge[v]:
                    if finished[v]:
                        continue

                    if seen[u] and finished[u] == 0:
                        cyc = [id]
                        while stc:
                            v, id = stc.pop()
                            if v == u:
                                break
                            cyc.append(id)
                        return cyc[::-1]

                    elif seen[u] == 0:
                        todo.append((1, u, id))
                        todo.append((0, u, id))

            else:
                if finished[v]:
                    continue
                stc.pop()
                finished[v] = 1

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
