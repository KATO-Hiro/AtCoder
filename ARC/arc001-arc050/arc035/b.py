# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    from collections import Counter


    n = int(input())
    t = sorted([int(input()) for _ in range(n)])

    # コンテストペナルティの総和：所要時間が小さい順に並べて，その累積和
    accumulated_t = list(accumulate([0] + t))
    total_t = sum(accumulated_t)
    print(total_t)

    # 並べ方：
    # 同じ所要時間の問題数を数える
    # 問題数!を計算してmod 10 ** 9 + 7を取る
    mod = 10 ** 9 + 7
    ans = 1
    c = Counter(t)

    for value in c.values():
        for i in range(1, value + 1):
            ans *= i
            ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
