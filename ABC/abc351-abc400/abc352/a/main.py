# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y, z = map(int, input().split())

    if x > y:
        x, y = y, x

    if x < z < y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
