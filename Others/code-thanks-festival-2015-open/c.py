# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n = int(input())
    h = list(map(int, input().split()))
    x = int(input())

    print(bisect(h, x) + 1)


if __name__ == '__main__':
    main()
