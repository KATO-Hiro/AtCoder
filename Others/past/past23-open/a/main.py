# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())

    if a > c and b > d:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
