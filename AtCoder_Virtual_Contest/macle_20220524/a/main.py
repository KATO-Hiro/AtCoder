# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = set([int(input()) for _ in range(n)])
    print(len(d))


if __name__ == "__main__":
    main()
