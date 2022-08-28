# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    print(s[n // 2])


if __name__ == "__main__":
    main()
