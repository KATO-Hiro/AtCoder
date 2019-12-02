# -*- coding: utf-8 -*-


def main():
    x = int(input())

    # dpによる解法
    # See:
    # https://atcoder.jp/contests/sumitrust2019/submissions/8726444
    dp = [False for _ in range(x + 200)]  # 配列を大きめに確保
    dp[0] = True  # 初期化

    for i in range(x + 10):
        if not dp[i]:
            continue

        # ある値に+100～+105できるとき
        for j in range(100, 106):
            dp[i + j] = True

    if dp[x]:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
