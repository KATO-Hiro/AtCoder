# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    rows = defaultdict(set)
    cols = defaultdict(set)
    naname1 = set()
    naname2 = set()

    for i in range(n):
        naname1.add(i * (n + 1) + 1)
        naname2.add(i * (n - 1) + n)

    for i, ai in enumerate(a, 1):
        row, col = divmod(ai - 1, n)
        rows[row].add(ai)
        cols[col].add(ai)

        if ai in naname1:
            naname1.discard(ai)
        if ai in naname2:
            naname2.discard(ai)

        if (
            len(rows[row]) == n
            or len(cols[col]) == n
            or len(naname1) == 0
            or len(naname2) == 0
        ):
            print(i)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
