# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = [0] * n
    y = [0] * n

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i] = xi + yi
        y[i] = xi - yi
    
    print(max(max(x) - min(x), max(y) - min(y)))


if __name__ == "__main__":
    main()
