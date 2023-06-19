# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    rows = list()
    cols = list()

    for ai in a:
        rows.append(sum(ai))

    for ai in zip(*a):
        cols.append(sum(ai))

    ans = list()

    for i in range(h):
        tmp = list()

        for j in range(w):
            tmp.append(rows[i] + cols[j] - a[i][j])

        ans.append(tmp)

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
