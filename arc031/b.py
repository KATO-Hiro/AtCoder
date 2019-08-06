# -*- coding: utf-8 -*-


def main():
    size = 10
    a = [list(input()) for _ in range(size)]
    land_count = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[False for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if a[j][i] == 'o':
                land_count += 1

    def dfs(x, y, count):
        if count == land_count + 1:
            return True

        visited[y][x] = True

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or 10 <= next_x or next_y < 0 or 10 <= next_y:
                continue

            if visited[next_y][next_x]:
                continue

            if a[next_y][next_x] == '○':
                dfs(next_x, next_y, count + 1)

        return

    for i in range(size):
        for j in range(size):
            if dfs(0, i, j):
                print('YES')
                exit()

    print('NO')


if __name__ == '__main__':
    main()
