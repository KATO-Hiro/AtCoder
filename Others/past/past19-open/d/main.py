# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, t = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    d = defaultdict(list)

    for ai, bi in ab:
        if ai not in d:
            d[ai] = [bi]
        else:
            d[ai].append(bi)

    a_max = max(d.keys())
    b_min = min(d[a_max])

    for ai, bi in ab:
        gi = t * (a_max - ai) + (bi - b_min)
        print(gi)


if __name__ == "__main__":
    main()
