# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, c = map(int, input().split())

    if (r == 2 or r == 14) and (2 <= c <= 14):
        print("white")
    elif (r == 3 or r == 13) and (c == 2 or c == 14):
        print("white")
    elif (r == 4 or r == 12) and (c == 2 or c == 14 or (4 <= c <= 12)):
        print("white")
    elif (r == 5 or r == 11) and (c == 2 or c == 14 or c == 4 or c == 12):
        print("white")
    elif (r == 6 or r == 10) and (c == 2 or c == 14 or c == 4 or c == 12 or (6 <= c <= 10)):
        print("white")
    elif (r == 7 or r == 9) and (c == 2 or c == 14 or c == 4 or c == 12 or c == 6 or c == 10):
        print("white")
    elif (r == 8) and (c % 2 == 0):
        print("white")
    else:
        print("black")


if __name__ == "__main__":
    main()
