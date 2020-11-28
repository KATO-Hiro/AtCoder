# -*- coding: utf-8 -*-


def solve(x, y):
    # 手数0: 同一の点
    if x == 0 and y == 0:
        return 0

    # 手数1: 問題文の定義
    if (x + y) == 0:
        return 1
    if (x - y) == 0:
        return 1
    if abs(x) + abs(y) <= 3:
        return 1

    # 手数2: 場合分け
    # 操作ABのパターン: パリティが一致するかどうか
    if (x + y) % 2 == 0:
        return 2
    # 操作CCのパターン: マンハッタン距離が6以下
    if abs(x) + abs(y) <= 6:
        return 2
    # 操作AC、BCのパターン
    if abs(x + y) <= 3:
        return 2
    if abs(x - y) <= 3:
        return 2

    # それ以外は、手数3
    return 3


def main():
    import sys

    input = sys.stdin.readline

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x = x2 - x1
    y = y2 - y1

    print(solve(x, y))


if __name__ == "__main__":
    main()
