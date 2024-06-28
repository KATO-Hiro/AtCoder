# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t = input().rstrip().split()

    if s == "AtCoder" and t == "Land":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
