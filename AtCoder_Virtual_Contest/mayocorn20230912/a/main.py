# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s.islower():
        print("a")
    else:
        print("A")


if __name__ == "__main__":
    main()
