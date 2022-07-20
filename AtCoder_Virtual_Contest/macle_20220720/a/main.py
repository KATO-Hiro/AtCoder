# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))

    if sum(a) >= 22:
        print("bust")
    else:
        print("win")


if __name__ == "__main__":
    main()
