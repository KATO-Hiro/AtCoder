# -*- coding: utf-8 -*-


# See
# https://atcoder.jp/contests/abc450/submissions/74271594
def encode(hi, wj, w):
    return hi * w + wj


def decode(n, w):
    return divmod(n, w)


def main():
    import sys
    from collections import deque, defaultdict

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    pending = -1
    sy, sx, gy, gx = pending, pending, pending, pending

    for i in range(h):
        for j in range(w):
            if s[i][j] == "S":
                sy, sx = i, j
            if s[i][j] == "G":
                gy, gx = i, j

    q = deque()
    prev = [[pending for _ in range(4)] for _ in range(h * w)]
    done = 10**6

    def push(cur_y, cur_x, di, prev_d):
        cur_pos = encode(cur_y, cur_x, w)

        if prev[cur_pos][di] != pending:
            return

        prev[cur_pos][di] = prev_d
        q.append((cur_pos, di))

    for i in range(4):
        push(sy, sx, i, done)

    while q:
        pos, dir = q.popleft()
        y, x = decode(pos, w)

        if (y, x) == (gy, gx):
            print("Yes")
            ans = []

            while prev[pos][dir] != done:
                ans.append("LRUD"[dir])
                prev_dir = prev[pos][dir]

                y -= dxy[dir][1]
                x -= dxy[dir][0]
                pos = encode(y, x, w)
                dir = prev_dir

            print("".join(ans[::-1]))
            exit()

        for j, (dx, dy) in enumerate(dxy):
            if s[y][x] == "o" and j != dir:
                continue
            if s[y][x] == "x" and j == dir:
                continue

            ny, nx = y + dy, x + dx

            if not (0 <= ny < h):
                continue
            if not (0 <= nx < w):
                continue
            if s[ny][nx] == "#":
                continue

            push(ny, nx, j, dir)

    print("No")


if __name__ == "__main__":
    main()
