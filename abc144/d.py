# -*- coding: utf-8 -*-


def main():
    from math import degrees, atan

    a, b, x = map(int, input().split())
    h = x / (a ** 2)
    y = 2 * h * a / b
    z = 2 * b - 2 * h

    # 水を入れたときの高さhを求める
    # 傾けたときにできる三角形の形状に注目
    if x == (a ** 2) * b:
        # 水筒が満タン
        print(0)
    elif 2 * h >= b:
        # 水筒が半分以上
        print(90 - degrees(atan(a / z)))
    else:
        print(degrees(atan(b / y)))


if __name__ == '__main__':
    main()
