# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n_max = 10 ** 5
    sizes = [[0 for _ in range(n_max + 1)] for _ in range(5)]
    dp = [0 for _ in range(5)]

    for _ in range(n):
        ti, xi, ai = map(int, input().split())

        if ti < xi:        
            continue

        sizes[xi][ti] = ai
    
    for i in range(1, n_max + 1):
        ndp = [0 for _ in range(5)]

        for j in range(5):
            if i < j:
                continue

            if j - 1 >= 0:
                ndp[j - 1] = max(ndp[j - 1], dp[j] + sizes[j - 1][i])
        
            ndp[j] = max(ndp[j], dp[j] + sizes[j][i])
            
            if j + 1 < 5:
                ndp[j + 1] = max(ndp[j + 1], dp[j] + sizes[j + 1][i])

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
