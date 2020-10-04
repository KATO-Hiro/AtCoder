# -*- coding: utf-8 -*-


def main():
    n, s = input().split()
    n = int(n)
    ans = 0

    # See:
    # https://atcoder.jp/contests/arc104/tasks/arc104_b/editorial

    # KeyInsight:
    # 文字列に含まれるAとT、およびCとGの個数が等しいときに条件を満たす

    # 「相補的」という用語の定義・性質を理解するのに時間を要した

    # △: どのように文字列の組み合わせの列挙を高速化するか
    # →制約から、左端を固定して全探索することができる
    # 条件がより厳しい場合は、連想配列に(AとCの個数の差、TとGの個数の差)という形で結果を保持

    # △: 文字の数をどのように数えるか
    # 例: カウント用の変数を2つ用意し、AとCのときは+1、TとGのときは-1とする
    # 管理する変数を減らす
    for i in range(n):
        a_count, t_count, c_count, g_count = 0, 0, 0, 0

        for j in range(i, n):
            if s[j] == "A":
                a_count += 1
            elif s[j] == "T":
                t_count += 1
            elif s[j] == "C":
                c_count += 1
            else:
                g_count += 1

            if (a_count == t_count) and (c_count == g_count):
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
