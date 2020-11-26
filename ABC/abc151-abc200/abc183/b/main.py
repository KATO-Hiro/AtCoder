# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    sx, sy, gx, gy = map(int, input().split())

    if gx < sx:
        sx, gx = gx, sx
        sy, gy = gy, sy

    ratio = sy / (sy + gy)
    ans = sx + (gx - sx) * ratio

    print(ans)


if __name__ == "__main__":
    main()
