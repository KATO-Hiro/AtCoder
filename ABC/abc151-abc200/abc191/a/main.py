# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    v, t, s, d = map(int, input().split())

    if (d < t * v) or (s * v < d):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
