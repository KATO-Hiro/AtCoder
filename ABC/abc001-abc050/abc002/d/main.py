# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai][bi] = True
        graph[bi][ai] = True

    ans = 1

    for bit in range(1, 1 << n):
        group = list()

        for j in range(n):
            if bit & 1 << j:
                group.append(j)

        flag = True

        for first, second in combinations(group, 2):
            if not graph[first][second]:
                flag = False

        if flag:
            ans = max(ans, len(group))

    print(ans)


if __name__ == "__main__":
    main()
