# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    if n == k:
        a = a + [x]
    else:
        a = a[:k] + [x] + a[k:]

    print(*a)


if __name__ == "__main__":
    main()
