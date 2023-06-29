# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    scores = defaultdict(int)

    # [left, right]ページに存在するai, biページのつながり
    for left in range(1, n + 1):
        for right in range(1, n + 1):
            for ai, bi in ab:
                if left <= ai and bi <= right:
                    scores[(left, right)] += 1

    pending = -1
    dp = [pending for _ in range(n + 1)]
    dp[0] = 0

    for _ in range(k):
        ndp = [pending for _ in range(n + 1)]

        for j in range(1, n + 1):
            for x in range(j):
                if dp[x] == pending:
                    continue

                ndp[j] = max(ndp[j], dp[x] + scores[(x + 1, j)])

        dp = ndp

    print(dp[n])


if __name__ == "__main__":
    main()
