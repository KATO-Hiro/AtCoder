# -*- coding: utf-8 -*-


def main():
    import sys
    from math import ceil

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**30
    ans = inf

    # a <= bと仮定
    for a in range(1, 10**6 + 1):
        b = ceil(m / a)

        if not (1 <= a <= n) or not (1 <= b <= n):
            continue

        ans = min(ans, a * b)

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
