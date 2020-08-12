# -*- coding: utf-8 -*-


def main():
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    def f(a, b, x, dx):
        return ((b - a) * dx) / x + a

    pos_sy = f(a, b, x, sx) - sy
    pos_ty = f(a, b, x, tx) - ty

    if pos_sy * pos_ty < 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
