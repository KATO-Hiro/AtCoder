# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    # 大きさを基準に昇順で並び替えておく
    a = sorted(list(map(int, input().split())))
    sum_a = list(accumulate([0] + a))
    # 色は最大でN種類
    ans = [False for _ in range(n)]
    # 初期化：最も大きいモンスターは，確実に最後まで生き残る
    ans[n - 1] = True

    # KeyInsight
    # あるモンスターiが最後まで残る
    # =吸収を繰り返していき，自分の2倍以上大きなモンスターが存在しないことを満たす，と言い換える
    # サイズの大きなモンスターから順に判定
    for i in range(n - 2, -1, -1):
        if a[i + 1] <= 2 * a[i]:
            if ans[i + 1]:
                ans[i] = True
        # サイズの小さいモンスターjは，事前に自分より小さいモンスターを全て吸収しておく
        # それからモンスターjとモンスターj+1のサイズを比較
        elif a[i + 1] <= 2 * sum_a[i + 1]:
            if ans[i + 1]:
                ans[i] = True
        else:
            ans[i] = False

    print(sum(ans))


if __name__ == '__main__':
    main()
