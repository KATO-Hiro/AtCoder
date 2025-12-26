# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    v = [list(map(int, input().split())) for _ in range(t)]

    for _ in range(t):
        print(0, 0, 0)


if __name__ == "__main__":
    main()
