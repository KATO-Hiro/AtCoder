# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0] * (w + 1)

    for wi, vi in wv:
        ndp = [0] * (w + 1)

        for j in range(w + 1):
            ndp[j] = max(ndp[j], dp[j])

            if j - wi >= 0:
                ndp[j] = max(ndp[j], dp[j - wi] + vi)

        dp = ndp
    
    print(dp[w])


if __name__ == "__main__":
    main()
