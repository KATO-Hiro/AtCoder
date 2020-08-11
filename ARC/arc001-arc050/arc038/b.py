# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    # See:
    # https://atcoder.jp/contests/arc038/submissions/6892990
    # 注：写経したため，自分の理解した範囲でコードの意図を言語化
    # マス(H, W)から(1, 1)に到達できるかどうかを判定
    dp = [[False for _ in range(w)] for _ in range(h)]

    # 実装は，0-index
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            # 到達できるかどうかを確認済み，もしくは障害物があるときは，更新しない
            if dp[i][j] or s[i][j] == '#':
                continue

            # 現在の位置から移動前の状態にできるかどうか
            # 3方向（問題文とは逆に，左・上・左上）それぞれ確認
            if i > 0:
                dp[i - 1][j] = True
            if j > 0:
                dp[i][j - 1] = True
            if i > 0 and j > 0:
                dp[i - 1][j - 1] = True

    # 初期位置に到達できたかどうか
    if dp[0][0]:
        print('First')
    else:
        print('Second')


if __name__ == '__main__':
    main()
