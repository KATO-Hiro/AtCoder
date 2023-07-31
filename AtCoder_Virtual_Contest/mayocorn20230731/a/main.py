# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    summed = 0

    for ai in a:
        summed += 1 / ai

    print(1 / summed)


if __name__ == "__main__":
    main()
