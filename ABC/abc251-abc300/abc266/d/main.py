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

    for k in range(t_max + 1):
        ti, xi, ai = t[k], x[k], a[k]

        ndp = [-inf] * count

        for i in range(count):
            if dp[i] == -inf:
                continue

            for j in range(max(0, i - 1), min(i + 1, min(k, 4)) + 1):
                if j == xi:
                    ndp[j] = max(ndp[j], dp[i] + ai)
                else:
                    ndp[j] = max(ndp[j], dp[i])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
