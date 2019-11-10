# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    d = list(map(int, input().split()))
    c = Counter(d)

    # KeyInsight
    # 条件を満たす個数：距離Diの頂点に対して親の個数の数だけ辺が張れるか，と言い換え

    # 気がつけた点
    # D1は0，それ以外は1l以上であるかどうかで場合分け
    # サンプルから組み合わせを愚直に数えた

    # 気がつけなかった点
    # 各距離における組み合わせを効率的に求める方法．重複組み合わせを数えようとしていた
    if d[0] == 1 or (0 in d[1:]):
        print(0)
        exit()

    ans = 1
    mod = 998244353

    for i in c.keys():
        if i >= 1:
            ans *= c[i - 1] ** c[i]
            ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
