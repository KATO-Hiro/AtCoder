# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    grid = [list(input().rstrip()) for _ in range(h)]
    sy, sx = -1, -1
    gy, gx = -1, -1

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "S":
                sy, sx = i, j
            elif grid[i][j] == "G":
                gy, gx = i, j

    inf = 10**18
    ans = inf
    dxy = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]

    for _ in range(2):
        d = deque()
        d.append((sy, sx))
        pending = inf
        dist = [[pending] * w for _ in range(h)]
        dist[sy][sx] = 0  # Initialize

        while d:
            y, x = d.popleft()

            if dist[y][x] == pending:
                continue

            # 現在のマスから次の移動方向を決める
            flag = (y + x) % 2

            for dx, dy in dxy[flag]:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                if grid[ny][nx] == "#":
                    continue
                if dist[ny][nx] != pending:
                    continue

                dist[ny][nx] = dist[y][x] + 1  # Update ans
                d.append((ny, nx))

        ans = min(ans, dist[gy][gx])
        # 進む方向を逆にする
        dxy[0], dxy[1] = dxy[1], dxy[0]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
