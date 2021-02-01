# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if a + c > b:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
