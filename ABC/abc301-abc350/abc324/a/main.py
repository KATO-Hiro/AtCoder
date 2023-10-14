# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = set(map(int, input().split()))

    if len(a) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
