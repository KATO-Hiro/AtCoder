# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, h, k = map(int, input().split())
    s = input().rstrip()
    d = defaultdict(int)

    for _ in range(m):
        xi, yi = map(int, input().split())
        d[(xi, yi)] += 1

    x, y = 0, 0

    for si in s:
        h -= 1

        if si == "R":
            x += 1
        elif si == "L":
            x -= 1
        elif si == "U":
            y += 1
        else:
            y -= 1

        if h < 0:
            print("No")
            exit()

        if (x, y) in d.keys() and d[(x, y)] >= 1 and h < k:
            h = k
            d[(x, y)] -= 1

    print("Yes")


if __name__ == "__main__":
    main()
