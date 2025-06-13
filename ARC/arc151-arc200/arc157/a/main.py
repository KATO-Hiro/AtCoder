# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b, c, d = map(int, input().split())

    if abs(b - c) > 1:
        print("No")
    elif abs(b - c) == 1:
        print("Yes")
    elif abs(b - c) == 0 and b > 0:
        print("Yes")
    elif a == 0 or d == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
