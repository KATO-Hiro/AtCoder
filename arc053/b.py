# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    from heapq import heappush, heappop

    s = input()
    s_dash = Counter(s)
    odds = list()
    operation_count = 0

    # a-zのうち，奇数個ある文字を探す
    for val in s_dash.values():
        if val % 2 == 1:
            odds.append(1)

        operation_count += val // 2

    # 全ての文字が偶数個のときは，X=|s|
    if len(odds) == 0:
        print(len(s))
        exit()

    # 奇数個の文字に対して，回文となるよう2個ずつ増やす
    # このとき，最小値をできるだけ大きくしたい&高速に操作するためヒープを使う
    for i in range(operation_count):
        value_min = heappop(odds)
        value_min += 2
        heappush(odds, value_min)

    print(min(odds))


if __name__ == '__main__':
    main()
