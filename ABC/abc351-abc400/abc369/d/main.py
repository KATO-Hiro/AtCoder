# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    # [倒した数 % 2]
    inf = 10**18
    dp = [-inf for _ in range(2)]
    dp[0] = 0

    for ai in a:
        ndp = [-inf for _ in range(2)]

        for j in range(2):
            # 逃す
            nj = j
            ndp[nj] = max(ndp[nj], dp[j])

            # 倒す
            nj = j ^ 1  # xorを使って反転させる
            x = ai * 2 if nj % 2 == 0 else ai
            ndp[nj] = max(ndp[nj], dp[j] + x)

        dp = ndp

    ans = max(dp)
    print(ans)


if __name__ == "__main__":
    main()
