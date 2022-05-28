# -*- coding: utf-8 -*-


def main():
    from statistics import median
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if median([a, b, c]) == b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
