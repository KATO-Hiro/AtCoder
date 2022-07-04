# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [int(input()) for _ in range(n)]
    judge = all(ai % 2 == 0 for ai in a)

    if judge:
        print("second")
    else:
        print("first")


if __name__ == "__main__":
    main()
