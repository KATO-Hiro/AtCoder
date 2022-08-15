# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    c = list(map(int, input().split()))
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(h):
        for j in range(w):
            aij = a[i][j]
            cij = c[aij - 1]
            y, x = i, j

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if (nx < 0) or (nx >= w) or (ny < 0) or (ny >= h):
                    continue
    
                ayx = a[ny][nx]

                if ayx == aij:
                    continue

                cyx = c[ayx - 1]

                if cyx == cij:
                    print("No")
                    exit()

    print("Yes")


if __name__ == "__main__":
    main()
