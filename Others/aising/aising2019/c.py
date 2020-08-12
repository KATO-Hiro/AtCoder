# -*- coding: utf-8 -*-
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
seen = [[False for __ in range(w)] for _ in range(h)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
black_count = 0
white_count = 0


def dfs(x: int, y: int):
    global black_count, white_count

    if s[x][y] == '#':
        black_count += 1
    else:
        white_count += 1

    seen[x][y] = True

    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if 0 <= next_x < h and 0 <= next_y < w:
            if s[x][y] != s[next_x][next_y] and not seen[next_x][next_y]:
                dfs(next_x, next_y)


def main():
    from sys import setrecursionlimit
    setrecursionlimit(200000)

    global black_count, white_count
    ans = 0

    # See:
    # http://drken1215.hatenablog.com/entry/2019/01/13/035500
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#' and not seen[i][j]:
                black_count = 0
                white_count = 0
                dfs(i, j)
                ans += black_count * white_count

    print(ans)


if __name__ == '__main__':
    main()
