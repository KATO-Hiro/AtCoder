# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if a <= b <= a * 6:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
