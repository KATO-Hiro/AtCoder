# -*- coding: utf-8 -*-


class Edge(object):

    def __init__(self, to, id):
        self.to = to
        self.id = id


def main():
    n = int(input())
    graph = [list() for _ in range(n)]

    for i in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        graph[ai].append(i)
        edge = Edge(ai, i)
        graph[bi].append(ai)


if __name__ == '__main__':
    main()
