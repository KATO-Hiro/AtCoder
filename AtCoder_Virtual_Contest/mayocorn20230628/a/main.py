# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = [int(input()) for _ in range(n)]
    print(len(set(d)))


if __name__ == "__main__":
    main()
