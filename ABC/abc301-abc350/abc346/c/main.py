# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for ai in a:
        if 1 <= ai <= k:
            d[ai] += 1

    ans = k * (k + 1) // 2

    keys = d.keys()

    if len(keys) >= 1:
        ans -= sum(keys)

    print(ans)


if __name__ == "__main__":
    main()
