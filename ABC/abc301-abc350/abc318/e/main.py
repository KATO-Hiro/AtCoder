# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    # 包除原理: (x, y, x) = (x, ?, x) - (x, x, x)

    # 1. 少なくともa[i]とa[k]が同じになる場合
    # iとkの位置を固定すると、jはk - i - 1通り
    # ΣΣ(k - i - 1): 外側のΣの添え字がk、内側のΣの添え字がi (+ i < k、かつ、a[i] = a[k])

    # 2重ループの高速化 = kを固定して、jの候補の部分を定数(とみなせるもの)と変数に分ける
    # Σ ((k - 1) * Σ(1) - Σi): 数列aの位置kを固定したときに、Σ(1)をa[i] (= a[k])となる個数、Σiをiの位置の総和
    count = defaultdict(int)
    summed = defaultdict(int)
    ans = 0

    for k in range(n):
        ak = a[k]
        ans += (k - 1) * count[ak] - summed[ak]

        count[ak] += 1
        summed[ak] += k

    # 2. 3変数が全て同じ場合 = mC3
    for i in count.keys():
        m = count[i]

        ans -= (m * (m - 1) * (m - 2)) // 6

    print(ans)


if __name__ == "__main__":
    main()
