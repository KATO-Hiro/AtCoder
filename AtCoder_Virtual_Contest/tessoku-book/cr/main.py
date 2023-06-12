# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    size = 10**5
    inf = 10**18
    dp = [inf] * (size + 1)
    dp[0] = 0

    for _ in range(n):
        wi, vi = map(int, input().split())
        ndp = [inf] * (size + 1)

        for i in range(size + 1):
            if dp[i] == inf:
                continue

            ndp[i] = min(ndp[i], dp[i])

            if i + vi > size:
                continue

            if dp[i] + wi > w:
                continue

            ndp[i + vi] = min(ndp[i + vi], dp[i] + wi)

        dp = ndp

    ans = 0

    for i, dp_i in enumerate(dp):
        if dp_i != inf:
            ans = i

    print(ans)


if __name__ == "__main__":
    main()
