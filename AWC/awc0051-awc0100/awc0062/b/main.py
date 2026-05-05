# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k, g = map(int, input().split())
    t = []

    for _ in range(n):
        _, ti = map(int, input().split())
        t.append(ti)

    acc = list(accumulate(t, initial=0))
    inf = 10**18
    candidate = inf

    for i in range(k, n + 1):
        now = acc[n] - (acc[i] - acc[i - k])
        candidate = min(candidate, now)

    ans = g + candidate
    print(ans)


if __name__ == "__main__":
    main()
