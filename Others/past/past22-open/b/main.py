# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, r = map(int, input().split())

    if r == 1:
        print("absent")
    elif w == 1:
        print("late")
    else:
        print("attend")


if __name__ == "__main__":
    main()
