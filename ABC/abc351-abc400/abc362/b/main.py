# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    d1 = (xb - xa) ** 2 + (yb - ya) ** 2
    d2 = (xc - xa) ** 2 + (yc - ya) ** 2
    d3 = (xc - xb) ** 2 + (yc - yb) ** 2
    d = [d1, d2, d3]
    d.sort()

    if d[0] + d[1] == d[2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
