# -*- coding: utf-8 -*-


def main():
    import sys
    from array import array
    from itertools import accumulate

    input = sys.stdin.readline

    h, w = map(int, input().split())
    q = int(input())

    # See:
    # https://atcoder.jp/contests/joi2011ho/submissions/13192811
    # J、O、Iをそれぞれ整数に置き換え
    # 1 << 20が設定されているのは、グリッドのマスの最大値よりも大きなダミー値だと思われる
    def encode(si):
        return (1 << 20) if si == "J" else 1 if si == "O" else 0

    # 行方向の累積和を取るためのヘルパー関数
    def add(array):
        return array[0] + array[1]

    grid = [[0] * (w + 1)]

    # See:
    # https://docs.python.org/ja/3/library/array.html
    # arrayをコンパクトに表現できるオブジェクト型。l: C言語のsigned long
    for _ in range(h):
        # 2次元累積和
        # 各行の先頭にダミー値を入れている
        grid.append(
            array(
                "l",
                list(
                    map(
                        add,
                        zip(grid[-1], accumulate(map(encode, "I" + input().rstrip()))),
                    )
                ),
            )
        )

    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        count = (
            grid[ci][di] - grid[ci][bi - 1] - grid[ai - 1][di] + grid[ai - 1][bi - 1]
        )
        jungles = count >> 20  # ダミー値を除外
        oceans = count & ((1 << 20) - 1)  # ダミー値を除外
        ices = (ci - ai + 1) * (di - bi + 1) - (jungles + oceans)
        print(jungles, oceans, ices)


if __name__ == "__main__":
    main()
