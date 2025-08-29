# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()

    for ai, bi in ab:
        print(ai, bi)


if __name__ == "__main__":
    main()
