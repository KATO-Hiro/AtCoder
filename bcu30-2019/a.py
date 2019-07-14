# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = sorted([int(input()) for _ in range(n)])
    print(sum(a[:n - k]) * 2 + sum(a[n - k:]))


if __name__ == '__main__':
    main()
