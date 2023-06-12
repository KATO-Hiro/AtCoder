# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        ai, bi = map(int, input().split())

        graph[ai].append(bi)
        graph[bi].append(ai)

    for i in range(1, n + 1):
        si = ", ".join(map(str, graph[i]))
        print("{}: {}{}{}".format(i, "{", si, "}"))


if __name__ == "__main__":
    main()
