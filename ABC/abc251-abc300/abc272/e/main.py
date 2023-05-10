# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from math import ceil

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [set() for _ in range(m)]

    # See:
    # https://atcoder.jp/contests/abc272/submissions/35477545
    # aiが0以上n未満となるまでの回数lower, upperを計算
    for i, ai in enumerate(a, 1):
        lower = max(0, ceil(-ai / i))
        ai += i * lower

        for j in range(lower, m + 1):
            if ai < m:
                s[j - 1].add(ai)
            else:
                break

            ai += i

    # mexを計算
    for i in range(m):
        ans = 0

        while ans in s[i]:
            ans += 1

        print(ans)


if __name__ == "__main__":
    main()
