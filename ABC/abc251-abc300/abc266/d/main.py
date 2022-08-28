# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = 10 ** 18
    size = 10 ** 5 + 10
    t, x, a = [0] * size, [0] * size, [0] * size

    for i in range(n):
        ti, xi, ai = map(int, input().split())
        t[ti], x[ti], a[ti] = ti, xi, ai
    
    count = 5
    dp = [-inf] * count
    dp[0] = 0
    t_max = max(t)

    for i in range(t_max):
        ni = i + 1  # ポイント
        ndp = [-inf] * count

        for j in range(count):
            for nj in range(j - 1, j + 2):
                # 遷移できない範囲を弾く
                if nj < 0 or nj >= count:
                    continue

                ndp[nj] = max(ndp[nj], dp[j])

        # ボーナスとして扱う
        ndp[x[ni]] += a[ni]

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
