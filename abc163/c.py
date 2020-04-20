# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = Counter(map(int, input().split()))
    keys = a.keys()

    for i in range(1, n + 1):
        if i in keys:
            print(a[i])
        else:
            print(0)


if __name__ == '__main__':
    main()
