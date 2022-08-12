# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]

    for ai, bi in sorted(ab, key=lambda x: (x[1], x[0])):
        print(ai, bi)


if __name__ == "__main__":
    main()
