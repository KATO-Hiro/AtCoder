# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    txa, tya, txb, tyb, t, v = list(map(int, input().split()))
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())
        dist = sqrt((y - tya) ** 2 + (x - txa) ** 2) + sqrt((tyb - y) ** 2 + (txb - x) ** 2)

        if dist <= v * t:
            print('YES')
            exit()

    print('NO')


if __name__ == '__main__':
    main()
