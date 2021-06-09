# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split("T")
    gx, gy = map(int, input().split())
    xs = list()
    ys = list()

    for index, si in enumerate(s):
        if index % 2 == 0:
            xs.append(len(si))
        else:
            ys.append(len(si))

    current_x = xs[0]
    current_y = 0

    for xi in sorted(xs[1:], reverse=True):
        if current_x > gx:
            current_x -= xi
        else:
            current_x += xi

    for yi in sorted(ys, reverse=True):
        if current_y > gy:
            current_y -= yi
        else:
            current_y += yi

    if current_x == gx and current_y == gy:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
