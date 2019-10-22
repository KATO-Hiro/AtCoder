# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    summed = 4 * n - m
    xy = list()

    # 2x + 3y + 4z = M
    #  x +  y +  z = N を解く
    # See:
    # https://atcoder.jp/contests/abc006/submissions/1112016
    # WAの原因：成立しない条件の境界値を0以下だと思っていた，2項目の条件に気がつけなかった
    if summed < 0:
        print(-1, -1, -1)
        exit()

    # xを決め打ち
    for x in range(summed // 2 + 1):
        y = summed - 2 * x

        if y >= 0:
            xy.append((x, y))

    for x, y in xy:
        z = n - (x + y)

        if z >= 0:
            print(x, y, z)
            exit()

    print(-1, -1, -1)


if __name__ == '__main__':
    main()
