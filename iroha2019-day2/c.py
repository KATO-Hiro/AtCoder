# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n = int(input())
    h = [int(input()) for _ in range(n)]
    set_h = sorted(set(h))

    for i in range(n):
        print(bisect(set_h, h[i]))


if __name__ == '__main__':
    main()
