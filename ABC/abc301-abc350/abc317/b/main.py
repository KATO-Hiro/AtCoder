# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))

    for ai, aj in zip(a, a[1:]):
        if aj - ai == 2:
            print(ai + 1)
            exit()


if __name__ == "__main__":
    main()
