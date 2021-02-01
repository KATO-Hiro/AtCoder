# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if c == 0:
        if a - b > 0:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if b - a > 0:
            print("Aoki")
        else:
            print("Takahashi")


if __name__ == "__main__":
    main()
