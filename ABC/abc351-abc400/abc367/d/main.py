# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(accumulate(a + a, initial=0))
    d = defaultdict(int)

    # 数列がmの倍数 => mod mの頻度を数える
    # mod mが同じ個数を数える + 差分更新
    for i in range(n):
        q = b[i] % m
        d[q] += 1

    ans = d[b[0]] - 1

    for j in range(1, n):
        q = b[j - 1] % m
        d[q] -= 1

        nq = b[j + n - 1] % m
        d[nq] += 1
        ans += d[b[j] % m] - 1

    print(ans)


if __name__ == "__main__":
    main()
