# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[0] == s[1]:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
