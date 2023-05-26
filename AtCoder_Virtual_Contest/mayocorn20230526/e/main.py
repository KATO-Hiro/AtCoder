# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 前計算: 1の位置がswapによって、どのように移動するか?
    s = [0] * m
    pos = 0

    for i, ai in enumerate(a):
        s[i] = pos
        ai -= 1

        if pos == ai:
            pos += 1
        elif pos == ai + 1:
            pos -= 1

    # シミュレーション: 逆順に + 前計算の結果と合成
    b = [i for i in range(1, n + 1)]
    ans = [0] * m

    for i in range(m - 1, -1, -1):
        ans[i] = b[s[i]]

        # swap
        ai = a[i] - 1
        b[ai], b[ai + 1] = b[ai + 1], b[ai]

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
