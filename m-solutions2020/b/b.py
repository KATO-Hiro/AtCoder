# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    k = int(input())
    count = 0

    while a >= b:
        b *= 2
        count += 1

    while b >= c:
        c *= 2
        count += 1

    if count <= k:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
