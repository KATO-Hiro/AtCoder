# -*- coding: utf-8 -*-


def main():
    import numpy as np

    n = int(input())
    # 通常のリストを生成する感覚で使える
    a = np.array([int(ai) for ai in input().split()])
    mod = 10 ** 9 + 7
    ans = 0

    # See:
    # https://img.atcoder.jp/abc147/editorial.pdf
    # KeyInsight:
    # XORを取る操作で各ビットは干渉しないため，それぞれ独立として扱ってよい
    # XORが1となるのは，Ai != Aj，つまり0と1の組み合わせを求めることと同じ

    # numpyを使うと実装が楽になる
    # See:
    # https://qiita.com/ZhangChaoran/items/0d59eb5c95cd9414801d
    for i in range(60):
        # a & 1で最下位のbitが0/1を判定している

        # 0でない個数を数える
        # See:
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.count_nonzero.html
        count = np.count_nonzero(a & 1)
        # 下からiビット目: bitが0の個数×同1の個数
        ans += (2 ** i) * (n - count) * count
        # b ビット右シフト
        # See:
        # http://www.tohoho-web.com/python/operators.html
        a >>= 1

    print(ans % mod)


if __name__ == '__main__':
    main()
