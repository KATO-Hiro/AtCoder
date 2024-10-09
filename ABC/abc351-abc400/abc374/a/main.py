# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s.endswith("san"):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
