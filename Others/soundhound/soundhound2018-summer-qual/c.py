# -*- coding: utf-8 -*-


def main():
    n, m, d = map(int, input().split())

    # KeyInsight
    # 期待値の線形性
    # See:
    # https://img.atcoder.jp/soundhound2018-summer-qual/editorial.pdf
    # https://mathtrain.jp/expectation

    # 気がつけた点
    # 愚直解を書き出した
    # 隣り合う2項がm - 1通りある

    # 解答までのギャップ
    # dが0かどうかで場合分け
    # 整数のペアを考える
    ans = m - 1

    if d == 0:
        # d = 0: (1, 1), ..., (n, n)のn通り
        ans /= n
    else:
        # d ≠ 0: (1, d + 1), ..., (n  -d, n)と(d - 1, 1), ..., (n, n - d)で2 * (n - d)通り
        ans *= 2 * (n - d)
        ans /= n ** 2

    print(ans)


if __name__ == '__main__':
    main()
