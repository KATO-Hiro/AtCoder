# -*- coding: utf-8 -*-


def main():
    n = int(input())
    # 1-indexに
    a = [0] + list(map(int, input().split()))
    c = [0 for _ in range(n + 1)]

    # See
    # https://www.youtube.com/watch?v=-o4r74eJzV4
    # 全体の計算量は，O(N^2)のようにみえて，O(NlogN)
    # 箱iの番号が大きいものから見る
    for i in range(n, 0, -1):
        # ボールの個数の和を0で初期化
        ball_count = 0

        # iの倍数の箱を順番に見る
        # ループの範囲を[2 * i, n]として，i個飛ばしで
        for j in range(2 * i, n + 1, i):
            # mod2は，xor（排他的論理和）を使うと言い換えるとスマートに記述できる．
            # ただし，演算の順序に注意が必要
            ball_count ^= c[j]

        # i個ずつみた後の合計(mod2)とa[i]を比べる
        c[i] = a[i] ^ ball_count

    # 出力
    # ボールが入っている箱の個数とその番号
    ans = [index for index, ci in enumerate(c) if ci == 1]
    print(len(ans))
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
