# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate, pairwise

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    c = list(map(int, input().split()))
    inf = 10**18
    ans = inf
    one_starts = [0] * n
    zero_starts = [0] * n

    # 前計算: コストの累積和
    for i, si in enumerate(s):
        if (i % 2 == 0 and si == "0") or (i % 2 == 1 and si == "1"):
            one_starts[i] = c[i]
        if (i % 2 == 0 and si == "1") or (i % 2 == 1 and si == "0"):
            zero_starts[i] = c[i]

    one_starts = list(accumulate(one_starts, initial=0))
    zero_starts = list(accumulate(zero_starts, initial=0))

    for i, (si, sj) in enumerate(pairwise(s), 1):
        # i, i + 1が'1'のパターン
        candidate1 = 0

        if si == "0":
            candidate1 += c[i - 1]
        if sj == "0":
            candidate1 += c[i]

        if i % 2 == 1:
            candidate1 += zero_starts[n] - zero_starts[min(n, i + 1)]
            candidate1 += one_starts[max(0, i - 1)]
        else:
            candidate1 += one_starts[n] - one_starts[min(n, i + 1)]
            candidate1 += zero_starts[max(0, i - 1)]

        ans = min(ans, candidate1)

        # i, i + 1が'0'のパターン
        candidate2 = 0

        if si == "1":
            candidate2 += c[i - 1]
        if sj == "1":
            candidate2 += c[i]

        if i % 2 == 1:
            candidate2 += one_starts[n] - one_starts[min(n, i + 1)]
            candidate2 += zero_starts[max(0, i - 1)]
        else:
            candidate2 += zero_starts[n] - zero_starts[min(n, i + 1)]
            candidate2 += one_starts[max(0, i - 1)]

        ans = min(ans, candidate2)

    print(ans)


if __name__ == "__main__":
    main()
