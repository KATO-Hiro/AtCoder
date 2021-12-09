# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    k = int(input())
    s = input().rstrip()

    count = s.count("R")

    if count == k:
        print("W")
    else:
        print("R")


if __name__ == "__main__":
    main()
