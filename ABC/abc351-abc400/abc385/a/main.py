# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = sorted(list(map(int, input().split())))

    if (a + b == c) or (a == b == c):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
