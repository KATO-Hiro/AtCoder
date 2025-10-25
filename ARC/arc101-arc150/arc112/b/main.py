# -*- coding: utf-8 -*-


def floor(number, divisor):
    return number // divisor if number >= 0 else -((-number) // divisor)


def main():
    import sys

    input = sys.stdin.readline

    b, c = map(int, input().split())

    # b, -bを起点として左右に移動できる位置を計算
    # 1. bから左
    value_min1 = b - floor(c, 2)

    # 2. -bから左
    value_min2 = -b - floor(c - 1, 2)
    # 3. -bから右 (1. の後で移動)
    value_max2 = -b + floor(c - 1, 2)

    # 4. bから右 (2. の後で移動)
    value_max1 = b + floor(c - 2, 2)

    # 区間の重複がある場合は除外
    if value_min1 <= value_max2 and value_min2 <= value_max1:
        value_min = min(value_min1, value_min2)
        value_max = max(value_max1, value_max2)
        print(value_max - value_min + 1)
    else:
        print((value_max1 - value_min1 + 1) + (value_max2 - value_min2 + 1))


if __name__ == "__main__":
    main()
