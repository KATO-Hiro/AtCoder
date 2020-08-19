# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    first = list()
    second = list()

    for i in range(m):
        ai, bi = map(int, input().split())

        if ai == 1:
            first.append(bi)

        if bi == n:
            second.append(ai)

    ans = set(first) & set(second)

    if len(ans) > 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
