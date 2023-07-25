# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    d = defaultdict(int)

    for ai, bi in ab:
        d[1] += bi
        d[ai + 1] -= bi

    prev = 0

    for key in sorted(d.keys()):
        cur = d[key] + prev

        if cur <= k:
            print(key)
            exit()

        prev = cur


if __name__ == "__main__":
    main()
