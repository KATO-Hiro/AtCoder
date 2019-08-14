# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    dxy = [(1, 0), (0, 1), (1, 1)]
    memo = [[None for _ in range(w)] for _ in range(h)]

    def is_lost(i, j) -> bool:
        # 盤外
        if i < 0 or h <= i or j < 0 or w <= j:
            return True

        # 障害物
        if s[i][j] == '#':
            return True

        return False

    def judge(i, j) -> str:
        # 基本ケース（終了条件）
        if is_lost(i, j):
            return True

        # 計算量削減のため，メモを利用（メモ化再帰）
        if memo[i][j] is not None:
            return memo[i][j]

        # 初期化
        result = False

        # 再帰ケース
        # 現在の位置(i, j)から下・右・右下の3方向に移動
        for dx, dy in dxy:
            nx = j + dx
            ny = i + dy

            if judge(ny, nx) is False:
                result = True

        # メモに記録して，次回以降はこの結果を使い回す
        memo[i][j] = result
        return memo[i][j]

    if judge(0, 0):
        print('First')
    else:
        print('Second')


if __name__ == '__main__':
    main()
