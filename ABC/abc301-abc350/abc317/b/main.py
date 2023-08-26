# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    prev = a[0]

    for ai in a[1:]:
        if ai - prev != 1:
            print(prev + 1)
            exit()

        prev = ai


if __name__ == "__main__":
    main()
