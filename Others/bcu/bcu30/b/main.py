# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    n = 9
    s = [list(input().rstrip()) for _ in range(n)]
    ok = True

    for si in s:
        if len(set(si)) != n:
            ok = False
            break

    for sj in rotate_90_degrees_to_right(s):
        if len(set(sj)) != n:
            ok = False
            break

    dxy = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-1, 2), (1, 2), (-2, 1), (2, 1)]

    for y in range(n):
        for x in range(n):
            for dx, dy in dxy:
                ny, nx = y + dy, x + dx

                if not (0 <= ny < n):
                    continue
                if not (0 <= nx < n):
                    continue
                if s[ny][nx] != s[y][x]:
                    continue

                ok = False
                break

    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
