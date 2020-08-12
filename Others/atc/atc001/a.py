# -*- coding: utf-8 -*-


def main():
    from sys import setrecursionlimit

    setrecursionlimit(300000)

    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    is_seen = [[False for _ in range(w)] for _ in range(h)]
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(h):
        for j in range(w):
            if c[i][j] == "s":
                start_x, start_y = j, i

            if c[i][j] == "g":
                end_x, end_y = j, i

    def dfs(x, y):
        is_seen[y][x] = True

        if x == end_x and y == end_y:
            print('Yes')
            exit()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_x > w - 1 or next_y < 0 or next_y > h - 1:
                continue

            if is_seen[next_y][next_x] or c[next_y][next_x] == '#':
                continue

            dfs(next_x, next_y)

        return 'No'

    print(dfs(start_x, start_y))


if __name__ == '__main__':
    main()
