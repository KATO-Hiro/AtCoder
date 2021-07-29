# -*- coding: utf-8 -*-


def main():
    from statistics import mean, median
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = list()
    y = list()
    
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    
    x_median = median(x)
    y_median = median(y)

    ans = 0

    for xi, yi in zip(x, y):
        ans += abs(x_median - xi) + abs(y_median - yi)
    
    print(int(ans))


if __name__ == "__main__":
    main()
