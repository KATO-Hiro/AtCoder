# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    size = [0] * n
    graph = [set() for _ in range(n)]
    count = n

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            ui, vi = qi[1:]
            ui -= 1
            vi -= 1

            graph[ui].add(vi)
            size[ui] += 1
            graph[vi].add(ui)
            size[vi] += 1

            if size[ui] == 1:
                count -= 1
            if size[vi] == 1:
                count -= 1
        else:
            vi = qi[1]
            vi -= 1

            for to in graph[vi]:
                graph[to].remove(vi)
                size[to] -= 1

                if size[to] == 0:
                    count += 1

            graph[vi] = set()

            if size[vi] != 0:
                size[vi] = 0
                count += 1

        print(count)


if __name__ == "__main__":
    main()
