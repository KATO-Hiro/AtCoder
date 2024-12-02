# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, p = map(int, input().split())
    r2 = 0.9 * r + 0.1 * p
    print(int(r2))


if __name__ == "__main__":
    main()
