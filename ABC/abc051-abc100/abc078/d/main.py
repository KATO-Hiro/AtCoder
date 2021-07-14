# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, z, w = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print(abs(a[-1] - w))
    else:
        print(max(abs(a[-1] - w), abs(a[-1] - a[-2])))


if __name__ == "__main__":
    main()
