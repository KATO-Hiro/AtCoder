# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = n - k
    b = a[m:] + a[:m]
    print(*b)


if __name__ == "__main__":
    main()
