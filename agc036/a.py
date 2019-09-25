# -*- coding: utf-8 -*-


def main():
    from math import ceil

    s = int(input())

    # See:
    # https://www.youtube.com/watch?v=eFQGwwdAVWg
    # KeyInsight
    # 1つ目の点を原点に固定する
    # 2つ目のx座標を10^9，3つ目のx座標を1で固定
    # 面積は外積で求められる |x2y3 - y2x3| / 2
    # y3 = [s / x2]
    # y2 = x2y3 - s
    y3 = ceil(s / 10 ** 9)
    y2 = ((10 ** 9) * y3) - s
    print(0, 0, 10 ** 9, y2, 1, y3)


if __name__ == '__main__':
    main()
