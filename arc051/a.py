# -*- coding: utf-8 -*-


def main():
    from math import hypot

    x1, y1, r = list(map(int, input().split()))
    x2, y2, x3, y3 = list(map(int, input().split()))

    if (x2 <= x1 - r) and (x1 + r <= x3) and (y2 <= y1 - r) and (y1 + r <= y3):
        print('NO')
    else:
        print('YES')

    # See:
    # https://beta.atcoder.jp/contests/arc051/submissions/1187476
    if hypot(x1 - x2, y1 - y2) > r or hypot(x1 - x3, y1 - y3) > r or hypot(x1 - x2, y1 - y3) > r or hypot(x1 - x3, y1 - y2) > r:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
