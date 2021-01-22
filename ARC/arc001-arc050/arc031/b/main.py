# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n = 10
    s = [list(input()) for _ in range(n)]

    land_count = 0
    dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for i in range(n):
        for j in range(n):
            if s[i][j] == "o":
                land_count += 1

    for i in range(n):
        for j in range(n):
            d = deque()
            d.append((j, i))
            visited = [[False for _ in range(n)] for _ in range(n)]
            visited[i][j] = True
            count = 0

            while d:
                dix, diy = d.popleft()

                for dx, dy in dxy:
                    nx = dix + dx
                    ny = diy + dy

                    if nx < 0 or nx > 9:
                        continue

                    if ny < 0 or ny > 9:
                        continue

                    if s[ny][nx] == "x":
                        continue

                    if visited[ny][nx]:
                        continue

                    visited[ny][nx] = True
                    d.append((nx, ny))
                    count += 1

            if count == land_count:
                print("YES")
                exit()

    print("NO")


if __name__ == "__main__":
    main()
