# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x, y = 0, 0

    for _ in range(n):
        xi, yi = map(int, input().split())
        x += xi
        y += yi

    if x > y:
        print("Takahashi")
    elif x < y:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
