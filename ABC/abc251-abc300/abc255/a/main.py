# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2)]

    print(a[r - 1][c - 1])


if __name__ == "__main__":
    main()
