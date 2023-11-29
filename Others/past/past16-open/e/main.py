# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[0] == "1" and all(si == "0" for si in s[1:]):
        print(len(s) - 1)
    else:
        print(len(s))


if __name__ == "__main__":
    main()
