# -*- coding: utf-8 -*-


def solve():
    h, w = map(int, input().split())
    s = list(input().rstrip())

    d_count = s.count("D")
    r_count = s.count("R")
    d = ["D"] * (h - 1 - d_count)
    r = ["R"] * (w - 1 - r_count)
    dr, rd = d + r, r + d
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    y_min = [h - 1] * w
    y_max = [0] * w
    y_min[0] = y_max[0] = 0

    for i, si in enumerate(s):
        if si == "D":
            y1 += 1
            y2 += 1
        elif si == "R":
            x1 += 1
            x2 += 1
        else:
            rdi = rd.pop()
            dri = dr.pop()

            if rdi == "D":
                y1 += 1
            else:
                x1 += 1

            if dri == "D":
                y2 += 1
            else:
                x2 += 1

        y_min[x1] = min(y_min[x1], y1)
        y_min[x2] = min(y_min[x2], y2)

        y_max[x1] = max(y_max[x1], y1)
        y_max[x2] = max(y_max[x2], y2)

    ans = 0

    for y_min_i, y_max_i in zip(y_min, y_max):
        ans += y_max_i - y_min_i + 1

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
