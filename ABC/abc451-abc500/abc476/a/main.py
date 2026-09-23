# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[-1] == "e":
        print(s + "r")
    else:
        print(s + "er")


if __name__ == "__main__":
    main()
