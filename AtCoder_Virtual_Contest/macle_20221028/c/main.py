# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    sx, sy, tx, ty = map(int, input().split())
    dx, dy = tx - sx, ty - sy
    ans = ""

    ans += "U" * dy
    ans += "R" * dx
    ans += "D" * dy
    ans += "L" * (dx + 1)
    ans += "U" * (dy + 1)
    ans += "R" * (dx + 1)
    ans += "DR"
    ans += "D" * (dy + 1)
    ans += "L" * (dx + 1)
    ans += "U"

    print(ans)


if __name__ == "__main__":
    main()
