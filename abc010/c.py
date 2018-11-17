# -*- coding: utf-8 -*-


def main():
    from math import hypot

    txa, tya, txb, tyb, t, v = list(map(int, input().split()))
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())

        # See:
        # https://beta.atcoder.jp/contests/abc010/submissions/1230259
        dist = hypot(x - txa, y - tya) + hypot(txb - x, tyb - y)

        if dist <= v * t:
            print('YES')
            exit()

    print('NO')


if __name__ == '__main__':
    main()
