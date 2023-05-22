# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    graph = [set() for _ in range(n)]
    count = n

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            ui, vi = qi[1:]
            ui -= 1
            vi -= 1

            graph[ui].add(vi)
            graph[vi].add(ui)

            if len(graph[ui]) == 1:
                count -= 1
            if len(graph[vi]) == 1:
                count -= 1
        else:
            vi = qi[1]
            vi -= 1

            for to in graph[vi]:
                graph[to].remove(vi)

                if len(graph[to]) == 0:
                    count += 1

            if len(graph[vi]) != 0:
                graph[vi] = set()
                count += 1

        print(count)


if __name__ == "__main__":
    main()
