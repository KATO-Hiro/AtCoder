# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    inf = 10**18
    size_max = 5 * 10**5 + 1
    dp = [-inf] * size_max
    zero = 500**2
    dp[zero] = 0

    for _ in range(n):
        wi, hi, bi = map(int, input().split())
        ndp = [-inf] * size_max

        for j in range(size_max):
            if dp[j] == -inf:
                continue

            nj1 = j - wi
            nj2 = j + wi

            if nj1 >= 0:
                ndp[nj1] = max(ndp[nj1], dp[j] + hi)
            if nj2 < size_max:
                ndp[nj2] = max(ndp[nj2], dp[j] + bi)

        dp = ndp

    ans = max(dp[zero:])
    print(ans)


if __name__ == "__main__":
    main()
