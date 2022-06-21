# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))


if __name__ == "__main__":
    main()
