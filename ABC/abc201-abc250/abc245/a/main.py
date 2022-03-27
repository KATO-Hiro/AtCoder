# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())

    if a < c:
        print("Takahashi")
    elif a == c and b <= d:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
