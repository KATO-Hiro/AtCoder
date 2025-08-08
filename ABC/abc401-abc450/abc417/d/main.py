# -*- coding: utf-8 -*-


from bisect import bisect_right


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    pab = [tuple(map(int, input().split())) for _ in range(n)]
    size = 1000
    dp = [[0] * (size + 1) for _ in range(n + 1)]

    for j in range(size + 1):
        dp[n][j] = j

    # Xi <= 500 を愚直に計算
    b = list()

    for i, (pi, ai, bi) in enumerate(pab[::-1], 1):
        for j in range(size + 1):
            ni = n - i

            if j <= pi:
                nj = j + ai
            else:
                nj = max(0, j - bi)

            dp[ni][j] = dp[ni + 1][nj]

        b.append(bi)

    q = int(input())
    acc = list(accumulate(b[::-1], initial=0))

    for _ in range(q):
        xi = int(input())

        if xi >= size:
            index = bisect_right(acc, xi - size)

            if index == n + 1:
                ans = xi - acc[n]
            else:
                ans = dp[index][xi - acc[index]]
        else:
            ans = dp[0][xi]

        print(ans)


if __name__ == "__main__":
    main()
