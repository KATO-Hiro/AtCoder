# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    a = 3 * x - y
    b = -x + 3 * y

    if a >= 0 and a % 8 == 0 and b >= 0 and b % 8 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
