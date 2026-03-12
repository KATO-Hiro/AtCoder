# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for ai in a:
        if ai < x:
            x = ai
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
