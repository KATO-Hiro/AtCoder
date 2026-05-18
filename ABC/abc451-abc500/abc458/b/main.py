# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    ans = [[0 for _ in range(w)] for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    for y in range(h):
        for x in range(w):
            count = 0

            for dx, dy in dxy:
                ny, nx = y + dy, x + dx

                if not (0 <= ny < h):
                    continue
                if not (0 <= nx < w):
                    continue

                count += 1

            ans[y][x] = count

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
