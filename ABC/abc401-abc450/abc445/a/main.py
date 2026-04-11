# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[0] == s[-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
