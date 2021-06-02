# -*- coding: utf-8 -*-


from sys import setrecursionlimit


def main():
    import sys

    input = sys.stdin.readline

    setrecursionlimit(10 ** 7)

    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    mod = 10 ** 9 + 7

    def dfs(current, rest_color, parent=-1):
        count = rest_color

        used_color_count = 1

        if parent != -1:
            used_color_count += 1

        for to in graph[current]:
            if to == parent:
                continue

            count *= dfs(to, k - used_color_count, current)
            count %= mod
            used_color_count += 1

        return count

    ans = dfs(0, k)

    print(ans)


if __name__ == "__main__":
    main()
