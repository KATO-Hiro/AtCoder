# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split("-")

    if len(s[0]) == 3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
