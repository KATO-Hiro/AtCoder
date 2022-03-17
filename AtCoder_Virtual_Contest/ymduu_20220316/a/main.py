# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = input().rstrip()

    if n.count("7") >= 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
