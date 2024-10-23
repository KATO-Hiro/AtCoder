# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()
    a, b = 0, 0

    for si, ti in zip(s, t):
        if si == "R" and ti == "P":
            b += 1
        elif si == "S" and ti == "P":
            a += 1
        elif si == "S" and ti == "R":
            b += 1

    print(a, b)


if __name__ == "__main__":
    main()
