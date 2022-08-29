# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    i = int(input())
    i -= 1
    print(s[i])


if __name__ == "__main__":
    main()
