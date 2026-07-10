# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    inf = 10**18
    dp = [-inf] * (w + 1)
    dp[0] = 0

    for _ in range(n):
        wi, vi = map(int, input().split())
        ndp = [-inf] * (w + 1)

        for j in range(w + 1):
            if dp[j] == -inf:
                continue

            ndp[j] = max(ndp[j], dp[j])

            nj = j + wi

            if nj > w:
                continue

            ndp[nj] = max(ndp[nj], dp[j] + vi)

        dp = ndp

    ans = max(dp)

    if ans == -inf:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
