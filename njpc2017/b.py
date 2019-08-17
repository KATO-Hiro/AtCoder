# -*- coding: utf-8 -*-


def main():
    from collections import deque

    h, w, n = map(int, input().split())
    link_max = h * (w - 1) + (h - 1) * w
    nodes = deque()
    visited = set()
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(n):
        ri, ci = map(int, input().split())
        nodes.append((ri, ci))

    while nodes:
        x, y = nodes.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if ny <= 0 or h < ny or nx <= 0 or w < nx:
                continue

            if (y, x, ny, nx) not in visited or (ny, nx, y, x) not in visited:
                print(y, x, ny, nx)
                # visited.add((y, x, ny, nx))

    # print(visited)


if __name__ == '__main__':
    main()
