# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    yx = [tuple(map(int, input().split())) for _ in range(n)]
    rows = defaultdict(set)
    cols = defaultdict(set)

    for i, (yi, xi) in enumerate(yx):
        rows[yi].add(i)
        cols[xi].add(i)

    q = int(input())

    for _ in range(q):
        type, now = list(map(int, input().split()))

        if type == 1:
            print(len(rows[now]))

            for id in rows[now]:
                _, xi = yx[id]
                cols[xi].discard(id)

            rows[now] = set()
        else:
            print(len(cols[now]))

            for id in cols[now]:
                yi, _ = yx[id]
                rows[yi].discard(id)

            cols[now] = set()


if __name__ == "__main__":
    main()
