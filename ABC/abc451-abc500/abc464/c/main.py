# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [[] for _ in range(m + 1)]
    c = Counter()

    for _ in range(n):
        ai, di, bi = map(int, input().split())

        if di == 1:
            ai = bi

        ab[di].append((ai, bi))
        c[ai] += 1

    ans = []

    for day in range(1, m + 1):
        for ai, bi in ab[day]:
            c[ai] -= 1

            if c[ai] == 0:
                del c[ai]

            c[bi] += 1

        ans.append(len(c.keys()))

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
