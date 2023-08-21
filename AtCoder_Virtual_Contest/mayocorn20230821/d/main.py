# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # 一部を固定して考える
    # ・対称性を利用
    #   ・Aの先頭、末尾の桁の値をそれぞれa_top、a_bottomとすると、
    #     指定された条件に基づいてBの先頭、末尾の桁の値はa_bottom、a_topとも表現できる

    # 同じ状態をまとめることで、愚直な足し算から掛け算で高速に処理できる
    # 求める答えは、Σ count[a_top][a_bottom] * count[a_bottom][a_top]
    # a: [1, n]を全探索して、先頭と末尾の値を取って集計
    size = 10
    count = [[0 for _ in range(size)] for _ in range(size)]

    for a in range(1, n + 1):
        sa = str(a)
        top, bottom = int(sa[0]), int(sa[-1])
        count[top][bottom] += 1

    ans = 0

    for top in range(1, size):
        for bottom in range(1, size):
            ans += count[top][bottom] * count[bottom][top]

    print(ans)


if __name__ == "__main__":
    main()
