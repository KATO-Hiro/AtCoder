# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    sum_x_y = abs(x) + abs(y)

    if sum_x_y <= n and (sum_x_y % 2 == n % 2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
