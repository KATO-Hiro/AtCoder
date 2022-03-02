# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if (b - a) == 1 or (a == 1 and b == 10):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
