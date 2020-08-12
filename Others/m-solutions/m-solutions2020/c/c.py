# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n - k):
        if a[i + k] > a[i]:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
