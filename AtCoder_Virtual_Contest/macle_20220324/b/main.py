# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, h, n = map(int, input().split())
    x_min = 0
    x_max = w
    y_min = 0
    y_max = h

    for i in range(n):
        xi, yi, ai = map(int, input().split())

        if ai == 1:
            x_min = max(x_min, xi)
        elif ai == 2:
            x_max = min(x_max, xi)
        elif ai == 3:
            y_min = max(y_min, yi)
        else:
            y_max = min(y_max, yi)

    dx = x_max - x_min
    dy = y_max - y_min
    
    if x_min > x_max:
        dx = 0
    if y_min > y_max:
        dy = 0

    print(dx * dy)


if __name__ == "__main__":
    main()
