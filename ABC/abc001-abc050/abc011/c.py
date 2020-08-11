# -*- coding: utf-8 -*-


def main():
    n = int(input())
    dp = [float('inf') for _ in range(n + 1)]
    ng_numbers = list()

    # See:
    # https://www.slideshare.net/chokudai/abc011
    for i in range(3):
        ng_number = int(input())

        if ng_number == n:
            print('NO')
            exit()

        ng_numbers.append(ng_number)

    # KeyInsight
    # 直前の状態にのみ依存している: DPの可能性がある
    # 気がつけなかった点：管理する状態を操作回数とする
    dp[n] = 0

    for i in range(n, -1, -1):
        if i in ng_numbers:
            continue

        # 範囲外参照を回避
        for j in range(1, 4):
            if i - j < 0:
                continue

            # 気がつけなかった点: 必要な操作回数を更新
            dp[i - j] = min(dp[i] + 1, dp[i - j])

    if dp[0] <= 100:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
