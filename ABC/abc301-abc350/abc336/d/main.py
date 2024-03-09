# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = n + 2
    # 便宜的に先頭と末尾に0を置く
    a = [0] + list(map(int, input().split())) + [0]
    b = a[::-1]
    height_left = [0] * m
    height_right = [0] * m

    # 現在の項は、直前の項 + 1より大きくはできないことに着目 (= 直前の結果を使って高速化)
    # 左右から実現可能な値の候補を列挙
    for i in range(1, n + 1):
        height_left[i] = min(height_left[i - 1] + 1, a[i])
        height_right[i] = min(height_right[i - 1] + 1, b[i])

    ans = 0

    for hl, hr in zip(height_left, height_right[::-1]):
        ans = max(ans, min(hl, hr))

    print(ans)


if __name__ == "__main__":
    main()
