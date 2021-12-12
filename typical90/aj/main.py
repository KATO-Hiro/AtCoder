# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = [0] * n
    y = [0] * n

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i] = xi + yi
        y[i] = xi - yi
    
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)
    
    for j in range(q):
        qi = int(input())
        qi -= 1

        xi = x[qi]
        yi = y[qi]

        print(max(x_max - xi, xi - x_min, y_max - yi, yi - y_min))


if __name__ == "__main__":
    main()
