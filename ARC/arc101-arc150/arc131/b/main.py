# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for y in range(h):
        for x in range(w):
            if c[y][x] != ".":
                continue

            colors = set()

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue

                if c[ny][nx] == ".":
                    continue

                colors.add(int(c[ny][nx]))
            
            for color in range(1, 6):
                if color not in colors:
                    c[y][x] = str(color)
                    break
    
    for ci in c:
        print("".join(ci))


if __name__ == "__main__":
    main()