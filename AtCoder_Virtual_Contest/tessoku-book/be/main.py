# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # 前計算: ダブリングで、2 ** j日後の位置を求めておく
    # j = 0のときは、aそのもの
    # jの上限を見積もる
    j_max = 30
    dp = [[0 for _ in range(n)] for _ in range(j_max)]

    for i, ai in enumerate(a):
        dp[0][i] = ai - 1

    for j in range(1, j_max):
        for i in range(n):
            dp[j][i] = dp[j - 1][dp[j - 1][i]]

    # yiを2進数に変換して、ビットが立っているときだけ位置を更新
    for _ in range(q):
        xi, yi = map(int, input().split())
        xi -= 1
        j = 0
        pos = xi

        while yi > 0:
            if yi & 1:
                pos = dp[j][pos]

            j += 1
            yi >>= 1

        print(pos + 1)


if __name__ == "__main__":
    main()
