# -*- coding: utf-8 -*-


def main():
    h, n = map(int, input().split())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    inf = float('inf')
    dp = [inf for _ in range(2 * 10 ** 4 + 100)]
    dp[0] = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

    for i in range(h):
        for j, ai in enumerate(a):
            if dp[i] == inf:
                continue

            dp[i + ai] = min(dp[i + ai], dp[i] + b[j])

    print(min(dp[h:]))


if __name__ == '__main__':
    main()
