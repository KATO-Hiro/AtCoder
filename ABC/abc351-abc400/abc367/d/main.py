# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a + a, initial=0))
    d = defaultdict(int)

    # 数列がmの倍数 => mod mの頻度を数える
    # mod mが同じ個数を数える + 差分更新
    for i in range(1, n):
        q = acc[i] % m
        d[q] += 1

    ans = 0

    # 答え → 頻度の順番で更新すると、シンプルに
    for j in range(n):
        ans += d[acc[j] % m]

        q = acc[j + 1] % m
        d[q] -= 1
        nq = acc[j + n] % m
        d[nq] += 1

    print(ans)


if __name__ == "__main__":
    main()
