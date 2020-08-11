# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # See:
    # https://www.youtube.com/watch?v=ENSOy8u9K9I&feature=youtu.be
    # KeyInsight:
    # 移動: 周期的ではない + 周期的に繰り返すの合計
    # 実装上のポイント
    # 経路と各点を通った順番を別々に管理する
    path = list()
    order = [-1 for _ in range(n + 1)]  # -1: 到達していない
    place = 1

    # 到達していない点がある限り、ループを繰り返す
    # = 同じ点を2回通るまで繰り返す
    while order[place] == -1:
        order[place] = len(path)  # ある場所を通った順番を管理
        path.append(place)  # 経路を更新
        place = a[place - 1]  # 次の行き先

    # 周期: 同じ点を2回通るまでに要した移動回数 - 周期に入るまでの移動回数
    cycle = len(path) - order[place]
    before_cycle_count = order[place]

    if (k < before_cycle_count):
        print(path[k])
    else:
        k -= before_cycle_count
        k %= cycle  # 周期: 途中の繰り返し部分を省いて、途中の部分だけ計算するようにする
        print(path[before_cycle_count + k])


if __name__ == '__main__':
    main()
