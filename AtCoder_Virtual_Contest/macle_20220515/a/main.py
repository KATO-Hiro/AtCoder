# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, a, b = map(int, input().split())

    if (-a + b) <= 0:
        print("delicious")
    elif (-a + b) <= x:
        print("safe")
    else:
        print("dangerous")


if __name__ == "__main__":
    main()
