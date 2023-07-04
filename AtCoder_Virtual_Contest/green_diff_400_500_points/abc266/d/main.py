# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t_max = 10**5 + 10
    x, a = [0] * t_max, [0] * t_max

    for _ in range(n):
        ti, xi, ai = map(int, input().split())
        x[ti], a[ti] = xi, ai
        t_max = ti

    dp = [0] * 5

    for i in range(1, t_max + 1):
        ndp = [0] * 5
        xi, ai = x[i], a[i]

        for j in range(5):
            for k in range(-1, 2):
                npos = j + k

                if i < 4 and npos > i:
                    continue

                if not (0 <= npos <= 4):
                    continue

                ndp[npos] = max(ndp[npos], dp[j] + ai * (npos == xi))

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
