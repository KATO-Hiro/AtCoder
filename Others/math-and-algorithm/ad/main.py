# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if x in a:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
