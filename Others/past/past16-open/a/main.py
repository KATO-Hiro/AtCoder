# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m = int(input())

    if 4 <= m <= 9:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
