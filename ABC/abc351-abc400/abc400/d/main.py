# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    sy, sx, ty, tx = map(lambda x: int(x) - 1, input().split())
    q = deque()
    inf = 10**18
    dist = [[inf for __ in range(w)] for _ in range(h)]
    visited = [[False for __ in range(w)] for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    # 01-BFSの問題と言い換え
    def push(y, x, d, cost):
        if not (0 <= y < h and 0 <= x < w):
            return
        if dist[y][x] <= d:
            return

        dist[y][x] = d

        if cost == 0:
            q.appendleft((y, x))
        else:
            q.append((y, x))

    push(sy, sx, 0, 0)

    while q:
        cur_y, cur_x = q.popleft()

        if visited[cur_y][cur_x]:
            continue

        visited[cur_y][cur_x] = True

        for dx, dy in dxy:
            ny, nx = cur_y + dy, cur_x + dx

            # 道 -> 道: コスト0
            if (0 <= ny < h and 0 <= nx < w) and s[ny][nx] == ".":
                push(ny, nx, dist[cur_y][cur_x], 0)

            # 道 -> 壁: コスト1
            push(cur_y + dy, cur_x + dx, dist[cur_y][cur_x] + 1, 1)
            push(cur_y + 2 * dy, cur_x + 2 * dx, dist[cur_y][cur_x] + 1, 1)

    ans = dist[ty][tx]
    print(ans)


if __name__ == "__main__":
    main()
