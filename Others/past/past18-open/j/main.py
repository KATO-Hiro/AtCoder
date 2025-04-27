# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    init_state = 0

    # 盤面の状態を2進数で表現(白:0, 黒:1)
    # BFSで盤面の状態を持つ
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                init_state |= 1 << (i * w + j)

    q = deque()
    q.append((0, 0, init_state, 0))  # i, j, state, cost
    used = set()
    used.add((0, 0, init_state))  # i, j, state
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    while q:
        y, x, state, cost = q.popleft()

        # 盤面が全て白
        if state == 0:
            print(cost)
            exit()

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h):
                continue
            if not (0 <= nx < w):
                continue

            # 移動先の盤面の状態を反転
            nstate = state ^ (1 << (ny * w + nx))

            if (ny, nx, nstate) in used:
                continue

            q.append((ny, nx, nstate, cost + 1))
            used.add((ny, nx, nstate))


if __name__ == "__main__":
    main()
