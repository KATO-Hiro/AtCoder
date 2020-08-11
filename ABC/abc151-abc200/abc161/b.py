# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    count = 0

    for ai in sorted(a, reverse=True):
        if (ai * 4 * m) >= total:
            count += 1

    if count >= m:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
