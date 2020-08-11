# -*- coding: utf-8 -*-


def main():
    a, b, x = map(int, input().split())

    # KeyInsight
    # 二分探索
    # 単調増加であるときに，特定の値を高速に調べることができる
    # See:
    # https://atcoder.jp/contests/abc146/submissions/8608718

    # 両端の値は必ず条件を満たす・満たさないものを初期値として与える
    left, right = 0, 10 ** 9 + 1

    def can_buy(value):
        return a * value + b * len(list(str(value))) <= x

    while right - left > 1:
        mid = (left + right) // 2

        if can_buy(mid):
            left = mid
        else:
            right = mid

    print(left)


if __name__ == '__main__':
    main()
