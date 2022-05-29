# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    mod = 998244353
    dp = [1] * m

    for i in range(n - 1):
        p = list(accumulate([0] + dp))
        ndp = [0] * m

        for j in range(m):
            ndp[j] += p[m]

            if k != 0:
                index_max = min(j + k, m)
                index_min = max(j - k + 1, 0)

                diff = p[index_max] - p[index_min]
                ndp[j] -= diff

            ndp[j] %= mod

        dp = ndp
    
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
