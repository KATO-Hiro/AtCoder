# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    large_h, large_w  = map(int, input().split())
    h, w  = map(int, input().split())

    if h >= large_h and w <= large_w:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
