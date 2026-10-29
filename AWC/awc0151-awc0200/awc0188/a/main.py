# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())

    if b >= n * a:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
