# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    q = int(input())
    rows = [i for i in range(n + 1)]
    cols = [i for i in range(n + 1)]
    t = 0  # 0: normal, 1: transposed

    def f(i, j):
        return n * (i - 1) + (j - 1)

    for _ in range(q):
        query = list(map(int, input().split()))
        qi = query[0]

        # 転置のときは、クエリのidを入れ替える
        if t == 1:
            if qi == 1:
                qi = 2
            elif qi == 2:
                qi = 1

        if qi == 1:
            ai, bi = query[1:]
            rows[ai], rows[bi] = rows[bi], rows[ai]
        elif qi == 2:
            ai, bi = query[1:]
            cols[ai], cols[bi] = cols[bi], cols[ai]
        elif qi == 3:
            t ^= 1
        else:
            ai, bi = query[1:]

            if t == 1:
                ai, bi = bi, ai

            row, col = rows[ai], cols[bi]
            print(f(row, col))


if __name__ == "__main__":
    main()
