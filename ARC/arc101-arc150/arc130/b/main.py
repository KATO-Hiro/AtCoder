# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, c, q = map(int, input().split())
    query = [tuple(map(int, input().split())) for _ in range(q)]
    rows, cols = set(), set()
    ans = [0] * (c + 1)

    for ti, ni, ci in query[::-1]:
        if ti == 1 and ni not in cols:
            ans[ci] += w - len(rows)
            cols.add(ni)
        elif ti == 2 and ni not in rows:
            ans[ci] += h - len(cols)
            rows.add(ni)

    print(*ans[1:])


if __name__ == "__main__":
    main()
