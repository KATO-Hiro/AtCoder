# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    sx, sy, tx, ty = map(int, input().split())
    dx, dy = tx - sx, ty - sy

    ans = dy * "U" + dx * "R" + dy * "D" + dx * "L"
    ans += "L"
    dx += 1
    dy += 1
    ans += dy * "U" + dx * "R" + "DR" + dy * "D" + dx * "L"
    ans += "U"
    print(ans)


if __name__ == "__main__":
    main()
