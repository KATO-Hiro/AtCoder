# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    b = list(map(int, input().split()))
    r = list(map(int, input().split()))

    print((sum(b) + sum(r)) / n)


if __name__ == "__main__":
    main()
