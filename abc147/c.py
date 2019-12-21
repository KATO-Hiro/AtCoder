# -*- coding: utf-8 -*-


def main():
    n = int(input())
    # 証言を有向グラフで管理，-1：証言なし
    graph = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        ai = int(input())

        for _ in range(ai):
            xi, yi = map(int, input().split())
            # 0-indexだと実装が楽に
            xi -= 1
            graph[i][xi] = yi

    ans = 0

    # See:
    # https://www.youtube.com/watch?v=tNyPYIhy9Ms&feature=youtu.be
    # KeyInsight：
    # あるパターンを決め打って，条件を満たすかどうかを判定する
    # 0/1で何を表現するか=>正直な人を1，不親切な人を0と割り当てる
    # 不親切な人=嘘つきではない

    # できた部分：正直な人と不親切な人をbitで割り当てて，全探索
    # できなかった部分: 正直な人と不親切な人の判定

    # bit全探索
    # ある人について，0/1を全て試す2^n通り
    for bit in range(1 << n):
        d = [0 for _ in range(n)]

        for j in range(n):
            # 0 1 0 0 1 ・・・のように，正直な人と不親切な人の集合を作成している
            # あるパターンのときにjビット目が1かどうかを判定
            if (bit >> j) & 1:
                d[j] = 1

        is_ok = True

        # 正直な人の証言が全て矛盾していないかを判断
        # 不親切な人の証言は判定しなくてもよいのがポイント
        for j in range(n):
            if d[j] == 1:
                for k in range(n):
                    # 該当する証言がない
                    if graph[j][k] == -1:
                        continue

                    # 証言とパターンの比較
                    if graph[j][k] != d[k]:
                        is_ok = False

        # 正直な人の最大値を更新
        if is_ok:
            ans = max(ans, sum(d))

    print(ans)


if __name__ == '__main__':
    main()
