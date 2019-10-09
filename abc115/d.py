# -*- coding: utf-8 -*-


def main():
    n, x = map(int, input().split())

    # KeyInsight
    # 再帰的な構造を見抜いて，条件に応じて場合分け
    # See:
    # http://drken1215.hatenablog.com/entry/2019/05/13/114600
    # ◯気がつけた点
    # ・バーガーとパティの量が，レベルが高くなるにつれて規則的に増える
    # ・再帰を使えば良さそう
    # △気がつけなかった点
    # ・規則性のある状態をどう再帰関数として，定式化するか
    def f(n, x):
        # 終了条件
        if n == 0:
            return 1

        # Nレベルバーガーから，N - 1レベルバーガーになるときの枚数の変化
        total_length = 2 ** (n + 1) - 3
        p_count = 2 ** n - 1

        # イメージ
        # B：バン，P：パティ
        # Nレベルバーガー：B(N - 1レベルバーガー)P(N - 1レベルバーガー)B
        if x == 1:
            # Bのみ
            return 0
        elif x <= total_length + 1:
            # B(N - 1レベルバーガー)
            # レベルを一つ減らす．N - 1レベルバーガーの中身を見るため，最下層のBは見なくてもよくなる
            return f(n - 1, x - 1)
        elif x <= total_length + 2:
            # B(N - 1レベルバーガー)P
            # N - 1レベルバーガーのパティ + 1枚
            return p_count + 1
        elif x <= 2 * (total_length + 1):
            # B(N - 1レベルバーガー)P(N - 1レベルバーガー)
            # N - 1レベルバーガーのパティ + 1枚と，上側にある（N - 1レベルバーガーのパティの数）
            return p_count + 1 + f(n - 1, x - total_length - 2)
        else:
            # B(N - 1レベルバーガー)P(N - 1レベルバーガー)B
            return 2 * p_count + 1

    print(f(n, x))


if __name__ == '__main__':
    main()
