# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m = int(input())
    d = list(map(int, input().split()))
    s = sum(d)
    half = (s + 1) // 2

    for i, di in enumerate(d, 1):
        e = min(di, half)
        half -= e

        if half == 0:
            print(i, e)
            exit()


if __name__ == "__main__":
    main()
