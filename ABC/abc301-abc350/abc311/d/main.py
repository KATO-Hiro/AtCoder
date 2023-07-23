# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    d = deque()
    d.append((1, 1))
    visited = [[False] * m for _ in range(n)]
    visited[1][1] = True
    # 停止したかどうかを管理
    stopped = [[False] * m for _ in range(n)]
    stopped[1][1] = True
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while d:
        y, x = d.popleft()

        for dx, dy in dxy:
            nx, ny = x, y

            while s[ny + dy][nx + dx] == ".":
                nx += dx
                ny += dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True

            if not stopped[ny][nx]:
                stopped[ny][nx] = True
                d.append((ny, nx))

    ans = sum([sum(row) for row in visited])
    print(ans)


if __name__ == "__main__":
    main()
