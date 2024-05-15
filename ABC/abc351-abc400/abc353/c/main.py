# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    a_max = 10**8
    ans = 0

    # 言い換え
    # (ai + aj) % 10 ** 8は、ai + aj か ai + aj - 10 ** 8のどちらか
    # Σ(ai + aj) - (10 ** 8) * 該当する個数

    # Σ(ai + aj) = Σ(ai * (n - 1))
    # グラフを書くとイメージしやすい
    for ai in a:
        ans += ai * (n - 1)

    # 該当するペアを全て試す = 数列を昇順にソートしても結果が変わらない
    # 二重ループの高速化 = 片方を全探索 + もう片方を二分探索
    right = n - 1

    for i in range(n):
        while right >= 0 and a[i] + a[right] >= a_max:
            right -= 1

        # i < jのみとなるように
        ans -= a_max * (n - 1 - max(i, right))
    print(ans)


if __name__ == "__main__":
    main()
