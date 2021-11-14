# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    colors = [-1] * n

    def dfs(pos, cur_color):
        colors[pos] = cur_color

        for to in graph[pos]:
            if colors[to] == -1:
                dfs(to, 1 - cur_color)
    
    dfs(0, 0)

    zero = colors.count(0)
    one = colors.count(1)

    if zero > one:
        print(*[index for index, color in enumerate(colors, 1) if color == 0][:n // 2])
    else:
        print(*[index for index, color in enumerate(colors, 1) if color == 1][:n // 2])


if __name__ == "__main__":
    main()
