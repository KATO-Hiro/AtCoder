# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    # 添字を誤読していた
    sy, sx = map(int, input().split())
    ty, tx = map(int, input().split())
    sy -= 1
    sx -= 1
    ty -= 1
    tx -= 1
    s = [input().rstrip() for _ in range(n)]

    # See:
    # https://atcoder.jp/contests/abc246/submissions/30639313
    dxy = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    dist = [[-1] * n for _ in range(n)]
    dist[sy][sx] = 0
    q = deque()
    q.append((sy, sx))

    while q:
        y, x = q.popleft()

        for dx, dy in dxy:
            ny = y + dy
            nx = x + dx

            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if s[ny][nx] == '#':
                    break
                if dist[ny][nx] != -1 and dist[ny][nx] <= dist[y][x]:
                    break

                if dist[ny][nx] < dist[y][x]:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                
                ny += dy
                nx += dx
    
    print(dist[ty][tx])


if __name__ == "__main__":
    main()
