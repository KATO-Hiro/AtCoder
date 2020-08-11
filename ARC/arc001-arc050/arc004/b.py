# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = [int(input()) for _ in range(n)]

    # 最大値：一直線に並んだときで，dの総和に等しい
    d_total = sum(d)
    print(d_total)

    d_max = max(d)
    exclude_d_max = d_total - max(d)

    # 最小値：最も長い辺の長さと，それ以外の辺の長さの和を比べて場合分け
    # サンプルが強い
    if d_max > exclude_d_max:
        print(d_max - exclude_d_max)
    else:
        print(0)


if __name__ == '__main__':
    main()
