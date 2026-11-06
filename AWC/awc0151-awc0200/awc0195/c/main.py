# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4] + [(0, 0)]
    q = int(input())

    for _ in range(q):
        ri, ci = map(int, input().split())
        ri -= 1
        ci -= 1

        for dx, dy in dxy:
            nx, ny = ci + dx, ri + dy

            if not (0 <= nx < w):
                continue
            if not (0 <= ny < h):
                continue

            if s[ny][nx] == "0":
                s[ny][nx] = "1"
            else:
                s[ny][nx] = "0"

    for si in s:
        print("".join(si))


if __name__ == "__main__":
    main()
