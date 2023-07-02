# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    ans = set()

    for i in range(h):
        for j in range(w):
            for dx, dy in dxy:
                nx = j + dx
                ny = i + dy

                if not (0 <= nx < w):
                    continue
                if not (0 <= ny < h):
                    continue

                b = a[i][j]
                nb = a[ny][nx]

                if nb < b:
                    b, nb = nb, b

                ans.add((b, nb))

    for xi, yi in sorted(ans):
        print(xi, yi)


if __name__ == "__main__":
    main()
