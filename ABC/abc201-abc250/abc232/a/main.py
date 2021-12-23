# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    print(int(s[0]) * int(s[2]))


if __name__ == "__main__":
    main()
