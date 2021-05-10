# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(accumulate([0] + list(map(int, input().split()))))

    for i in range(k, n + 1):
        print(a[i] - a[i - k])


if __name__ == "__main__":
    main()
