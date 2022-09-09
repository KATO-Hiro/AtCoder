# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    ab, cd = a + b, c + d

    if ab > cd:
        print("Left")
    elif ab == cd:
        print("Balanced")
    else:
        print("Right")


if __name__ == "__main__":
    main()
