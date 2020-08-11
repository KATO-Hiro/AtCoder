# -*- coding: utf-8 -*-


def main():
    from collections import deque

    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    dist = [[-1 for __ in range(w)] for _ in range(h)]
    blacks = deque()

    # See:
    # http://drken1215.hatenablog.com/entry/2019/05/05/223200?_ga=2.177845805.987014750.1556545680-1855989383.1556545680
    # https://blog.kichi2004.jp/2019/05/agc033/
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                dist[i][j] = 0
                blacks.append((i, j))

    while blacks:
        current = blacks.popleft()
        cur_x = current[1]
        cur_y = current[0]

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x < 0 or next_x >= w or next_y < 0 or next_y >= h:
                continue

            if dist[next_y][next_x] == -1:
                dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                blacks.append((next_y, next_x))

    ans = 0

    for i in range(h):
        for j in range(w):
            ans = max(ans, dist[i][j])

    print(ans)


if __name__ == '__main__':
    main()
