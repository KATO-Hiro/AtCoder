# -*- coding: utf-8 -*-


def main():
    from collections import deque

    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    cs = [list(input()) for _ in range(r)]

    dist = [[-1 for __ in range(c)] for _ in range(r)]
    dist[sy - 1][sx - 1] = 0
    q = deque()
    q.append((sy - 1, sx - 1))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if (next_y < 0 or r <= next_y) or (next_x < 0 or c <= next_x):
                continue

            if cs[next_y][next_x] == '#':
                continue

            if dist[next_y][next_x] != -1:
                continue

            dist[next_y][next_x] = dist[cur_y][cur_x] + 1
            q.append((next_y, next_x))

    print(dist[gy - 1][gx - 1])


if __name__ == '__main__':
    main()
