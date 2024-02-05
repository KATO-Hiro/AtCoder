# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split(".")
    print(s[-1])


if __name__ == "__main__":
    main()
