# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    s = input().rstrip().split("-")

    if len(s[0]) == a and len(s[1]) == b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
