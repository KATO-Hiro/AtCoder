# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(int)

    for i in range(m):
        tmp = list(map(int, input().split()))
        x = tmp[1:]

        for x1, x2 in combinations(x, 2):
            d[(x1, x2)] += 1
            d[(x2, x1)] += 1
    
    expected = n * (n - 1)

    if len(d.keys()) == expected:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
