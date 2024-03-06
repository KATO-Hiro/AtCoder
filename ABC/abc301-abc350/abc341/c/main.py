# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    t = input().rstrip()
    s = [list(input().rstrip()) for _ in range(h)]
    ans = 0

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            ok = True

            if s[y][x] == "#":
                continue

            ny, nx = y, x

            for ti in t:
                if ti == "L":
                    nx -= 1
                elif ti == "R":
                    nx += 1
                elif ti == "U":
                    ny -= 1
                else:
                    ny += 1

                if not (1 <= ny < h - 1):
                    ok = False
                    break
                if not (1 <= nx < w - 1):
                    ok = False
                    break
                if s[ny][nx] == "#":
                    ok = False
                    break

            if ok:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
