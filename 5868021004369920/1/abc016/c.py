# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n, m = map(int, input().split())
    graph = dict()

    for i in range(m):
        ai, bi = map(int, input().split())

        if ai not in graph.keys():
            graph[ai] = [bi]
        else:
            graph[ai].append(bi)

        if bi not in graph.keys():
            graph[bi] = [ai]
        else:
            graph[bi].append(ai)

    def is_included(parent, target):
        if target not in graph[parent]:
            return False
        else:
            return True

    def bfs(number):
        q = deque()
        q += graph[number]
        searched = []
        count = 0

        while q:
            person = q.popleft()

            if person not in searched:
                if not is_included(number, person):
                    count += 1
                else:
                    q += graph[person]
                    searched.append(person)

        return count

    for i in range(1, n + 1):
        print(bfs(i))


if __name__ == '__main__':
    main()
