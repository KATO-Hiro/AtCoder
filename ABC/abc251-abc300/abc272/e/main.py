# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from math import ceil

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    # aiが0以上n未満となるまでの回数lower, upperを計算
    for i in range(1, n + 1):
        ai = a[i - 1]
        ai += i  # 1回目の加算を行っておく

        if ai >= 0:
            lower = 0
        else:
            lower = ceil(-ai / i)

        if ai >= n:
            upper = 0
        else:
            upper = ceil((n - ai) / i)
            upper = min(upper, m)  # 配列外参照を防ぐ

        for j in range(lower, upper):
            d[j].append(ai + i * j)

    for i in range(m):
        # mexを計算
        di = d[i]
        size = len(di)
        exist = [False] * (size + 1)

        for dij in di:
            if dij <= size:  # mexの定義に従い、範囲外参照を防ぐ
                exist[dij] = True

        ans = 0

        while exist[ans]:
            ans += 1

        print(ans)


if __name__ == "__main__":
    main()
