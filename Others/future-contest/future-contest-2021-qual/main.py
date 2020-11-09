# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    xy = list()

    for i in range(100):
        xi, yi = map(int, input().split())
        xy.append((xi, yi))

    ans = "D" * xy[0][0]
    ans += "R" * xy[0][1]
    ans += "I"

    for (x1, y1), (x2, y2) in zip(xy, xy[1:]):
        if x2 > x1:
            ans += "D" * (x2 - x1)

            if y2 > y1:
                ans += "R" * (y2 - y1)
            else:
                ans += "L" * (y1 - y2)
        else:
            ans += "U" * (x1 - x2)

            if y2 > y1:
                ans += "R" * (y2 - y1)
            else:
                ans += "L" * (y1 - y2)

        ans += "I"

    print(ans)


if __name__ == "__main__":
    main()
