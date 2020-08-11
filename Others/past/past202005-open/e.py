# -*- coding: utf-8 -*-


def main():
    n, m, q = map(int, input().split())
    graph = [[] for _ in range(n)]

    for i in range(m):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1

        graph[ui].append(vi)
        graph[vi].append(ui)

    c = list(map(int, input().split()))

    for j in range(q):
        s = input().split()
        x = int(s[1]) - 1
        print(c[x])

        if s[0] == '1':
            for g in graph[x]:
                c[g] = c[x]
        else:
            y = int(s[2])
            c[x] = y


if __name__ == '__main__':
    main()
