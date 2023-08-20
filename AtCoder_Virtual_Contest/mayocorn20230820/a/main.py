# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if -(2**31) <= n < 2**31:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
