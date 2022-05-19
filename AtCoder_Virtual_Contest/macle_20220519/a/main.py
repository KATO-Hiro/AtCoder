# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = input().rstrip().split()

    if a == b:
        print("H")
    else:
        print("D")


if __name__ == "__main__":
    main()
