# -*- coding: utf-8 -*-


def is_cross(xi, yi, ri, xj, yj, rj):
    dist = abs(xi - xj) ** 2 + abs(yi - yj) ** 2

    if rj > ri:
        ri, rj = rj, ri
 
    if (ri - rj) ** 2 > dist:
        return 1
    if (ri - rj) ** 2 == dist:
        return 2
    elif (ri - rj) ** 2 < dist < (ri + rj) ** 2:
        return 3
    elif dist == (ri + rj) ** 2:
        return 4
    elif dist > (ri + rj) ** 2:
        return 5


def main():
    import sys

    input = sys.stdin.readline

    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())

    print(is_cross(x1, y1, r1, x2, y2, r2))


if __name__ == "__main__":
    main()
