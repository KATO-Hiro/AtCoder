# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ai in enumerate(a, 1):
        d[ai].append(i)

    inf = 10**18
    ans = inf

    for values in d.values():
        if len(values) <= 1:
            continue

        for first, second in pairwise(values):
            candidate = second - first + 1
            ans = min(ans, candidate)

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
