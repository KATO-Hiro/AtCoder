# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]
    b = [list(input().rstrip()) for _ in range(h)]

    for dy in range(h):
        for dx in range(w):
            ok = True

            for y in range(h):
                for x in range(w):
                    nx = (x + dx) % w
                    ny = (y + dy) % h

                    if a[ny][nx] != b[y][x]:
                        ok = False
                        break

            if ok:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
