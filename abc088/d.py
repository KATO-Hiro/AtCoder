# -*- coding: utf-8 -*-


def main():
    from collections import deque

    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    dist = [[float('inf') for _ in range(w)] for _ in range(h)]
    is_visited = [[False for _ in range(w)] for _ in range(h)]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    white_count = 0

    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                white_count += 1

    # スコアの最大化：全ての白マス－最短距離で(H, W)まで移動するのに必要なマスの数
    # BFS
    # Initialize
    d = deque()
    d.append(tuple((0, 0)))
    dist[0][0] = 1
    is_visited[0][0] = True

    while d:
        di = d.popleft()

        for dy, dx in dxy:
            nx = dx + di[1]
            ny = dy + di[0]

            if (nx < 0 or w <= nx or ny < 0 or h <= ny):
                continue
            elif s[ny][nx] == '#':
                continue
            elif is_visited[ny][nx]:
                continue
            else:
                dist[ny][nx] = dist[di[0]][di[1]] + 1
                is_visited[ny][nx] = True
                d.append((ny, nx))

    if dist[h - 1][w - 1] == float('inf'):
        print(-1)
    else:
        print(white_count - dist[h - 1][w - 1])


if __name__ == '__main__':
    main()
