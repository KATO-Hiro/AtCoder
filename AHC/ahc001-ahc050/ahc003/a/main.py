# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    for _ in range(1000):
        sy, sx, ty, tx = map(int, input().split())

        dy, dx = ty - sy, tx - sx
        ans = ""

        if dy > 0:
            ans += "D" * dy
        elif dy < 0:
            ans += "U" * abs(dy)

        if dx > 0:
            ans += "R" * dx
        elif dx < 0:
            ans += "L" * abs(dx)

        print(ans, flush=True)

        _ = int(input())


if __name__ == "__main__":
    main()
