# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    inf = -1
    dp = [inf] * (w + 1)
    dp[0] = 0

    for i in range(n):
        wi, vi = map(int, input().split())
        ndp = [0] * (w + 1)

        for j in range(w + 1):
            if dp[j] == inf:
                continue

            ndp[j] = max(ndp[j], dp[j])

            if j + wi > w:
                continue

            ndp[j + wi] = max(ndp[j + wi], dp[j] + vi)

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
