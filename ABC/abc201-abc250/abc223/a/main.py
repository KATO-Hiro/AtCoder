# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    if x >= 100 and x % 100 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
