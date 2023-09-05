# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d, n = map(int, input().split())
    t = [int(input()) for _ in range(d)]
    abc = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)

    for i in range(1, d):
        t_first, t_second = t[i - 1], t[i]
        ndp = [0] * (n + 1)

        for first, (aj, bj, cj) in enumerate(abc):
            if not (aj <= t_first <= bj):
                continue

            for second, (ak, bk, ck) in enumerate(abc):
                if not (ak <= t_second <= bk):
                    continue

                ndp[second] = max(ndp[second], dp[first] + abs(cj - ck))

        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
