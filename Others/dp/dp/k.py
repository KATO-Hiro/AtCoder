# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0 for _ in range(k + 1)]  # Firstが到達できるかどうかを管理

    # 石を順番に積み上げる(石を取り去る，を言い換え)
    # See:
    # https://atcoder.jp/contests/dp/submissions/3956066
    for i in range(k):
        # 既にFirstが到達可能な場合
        if dp[i]:
            continue

        # ある個数から，集合Aをすべて試す
        for ai in a:
            # k個より大きくなったら，計算を打ち切る
            # 範囲外参照を防ぐため
            if i + ai > k:
                break

            # 更新
            dp[i + ai] = 1

    if dp[-1] == 1:
        print('First')
    else:
        print('Second')


if __name__ == '__main__':
    main()
