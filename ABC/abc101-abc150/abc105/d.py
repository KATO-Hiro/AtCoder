# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    summed = [0 for _ in range(n + 1)]
    d = defaultdict(int)

    # See:
    # https://www.youtube.com/watch?v=7bbIZTIeDZM
    # KeyInsight:
    # 愚直解から計算量を減らす工夫
    # ◯: 1. 任意の要素数の和を計算、O(N)→累積和、前計算が(N)・各クエリの処理がO(1)
    # ◯: 2. mの倍数→mod m = 0
    # △: modの世界に対する理解
    #    累積和のうち、x, y番目の値a, bの差がmで割り切れる
    #    (b - a) mod m == 0
    #    a mod m == b mod mとなる
    #    mで割った余りが一致する個数を数えればよい
    for i in range(n):
        summed[i + 1] = (summed[i] + a[i]) % m

    ans = 0

    # ある地点jにおいて、mで割った余りが一致する個数を数える
    for j in range(n + 1):
        ans += d[summed[j]]
        d[summed[j]] += 1

    print(ans)


if __name__ == '__main__':
    main()
