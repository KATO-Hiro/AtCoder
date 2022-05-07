# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, large_w = map(int, input().split())
    w = [0] * (n)
    v = [0] * (n)

    for i in range(n):
        w[i], v[i] = map(int, input().split())
    
    # See:
    # https://atcoder.jp/contests/abc060/submissions/1253016
    # 物の重さをリスト・配列ではなく、defaultdictで管理
    dp = defaultdict(int)
    dp[0] = 0

    for i in range(n):
        ndp = defaultdict(int)

        for j in dp.keys():
            # i番目の物を選ぶ
            if (j + w[i]) <= large_w:
                ndp[j + w[i]] = max(ndp[j + w[i]], dp[j] + v[i])

            # i番目の物を選ばない
            ndp[j] = max(ndp[j], dp[j])

        dp = ndp
    
    print(max(dp.values()))


if __name__ == "__main__":
    main()
