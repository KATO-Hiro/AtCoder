# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    md = tuple(map(int, input().split()))
    gothec = [(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)]

    if md in gothec:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
