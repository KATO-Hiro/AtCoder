# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    a = list(accumulate([0] + [i for i in range(n + 1)]))
    ans = 0

    # KeyInsight:
    # 10 ** 100は実質、スルーしてよい
    # 0〜Nを順に並べた数列を考える
    # 左端からk個の組み合わせが最小値、右端からk個の組み合わせが最大値
    # 最小値〜最大値までの値を取る
    # k個の和を毎回取ると計算量がO(N ** 2)になるので、累積和を取る
    for j in range(k, n + 2):
        max_value = a[-1] - a[n + 1 - j]
        min_value = a[j]
        ans += (max_value - min_value) + 1
        ans %= mod

    print(ans % mod)


if __name__ == '__main__':
    main()
