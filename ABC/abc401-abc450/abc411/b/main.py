# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    d = list(map(int, input().split()))

    for i in range(n - 1):
        a = list(accumulate(d[i:]))
        print(*a)


if __name__ == "__main__":
    main()
