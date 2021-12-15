# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s1 = input().rstrip()
    s2 = input().rstrip()
    s = s1 + s2

    if s == "#..#" or s == ".##.":
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
