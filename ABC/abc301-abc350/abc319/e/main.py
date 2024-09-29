# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    n -= 1
    p, t = [0] * n, [0] * n

    for i in range(n):
        pi, ti = map(int, input().split())
        p[i], t[i] = pi, ti

    patterns = 840
    memo = [0] * patterns

    for pattern in range(patterns):
        now = pattern + x

        for pi, ti in zip(p, t):
            _, b = divmod(now, pi)

            now += (pi - b) % pi
            now += ti

        now += y
        memo[pattern] = now - pattern

    q = int(input())
    ans = [0] * q

    for i in range(q):
        now = int(input())
        now += memo[now % patterns]
        ans[i] = now

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
