# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())

    if 400 * w >= h**2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
