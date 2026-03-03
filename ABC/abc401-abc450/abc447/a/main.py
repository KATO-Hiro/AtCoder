# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    if n % 2 == 1:
        n += 1

    if m * 2 <= n:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
