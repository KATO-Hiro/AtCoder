# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    if len(set(s)) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
