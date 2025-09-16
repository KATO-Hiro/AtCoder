# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    if x in a:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
