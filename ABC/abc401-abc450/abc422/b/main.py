# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    for y in range(h):
        for x in range(w):
            if s[y][x] == ".":
                continue

            count = 0

            for dy, dx in dxy:
                ny = y + dy
                nx = x + dx

                if not (0 <= ny < h):
                    continue
                if not (0 <= nx < w):
                    continue
                if s[ny][nx] == ".":
                    continue

                count += 1

            if not (count == 2 or count == 4):
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
