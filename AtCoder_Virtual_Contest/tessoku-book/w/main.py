# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    # i枚目のクーポンを選んで、無料で購入できる商品の集合がSのときのクーポンの使用枚数の最小値
    inf = 10**9
    dp = [inf] * (1 << n)
    dp[0] = 0

    for i, ai in enumerate(a):
        ai = int("".join(map(str, ai[::-1])), 2)
        ndp = [inf] * (1 << n)

        for s in range(1 << n):
            if dp[s] == inf:
                continue

            ndp[s] = min(ndp[s], dp[s])
            ndp[s | ai] = min(ndp[s | ai], dp[s] + 1)

        dp = ndp

    ans = dp[(1 << n) - 1]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
