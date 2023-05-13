# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    prev = 0

    for hi in h:
        if hi > prev:
            prev = hi
        else:
            print(prev)
            exit()

    print(prev)


if __name__ == "__main__":
    main()
