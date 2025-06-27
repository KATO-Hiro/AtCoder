# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    p = input().rstrip()
    m = len(p)
    l = int(input())

    if m >= l:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
