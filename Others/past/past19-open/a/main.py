# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, h, m = map(int, input().split())

    x -= m

    if x < 0:
        x += 60

    print(x)


if __name__ == "__main__":
    main()
