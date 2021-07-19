# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    row = [0 for _ in range(h)]
    column = [0 for _ in range(w)]

    for i in range(h):
        for j in range(w):
            row[i] += a[i][j]
            column[j] += a[i][j]

    ans = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            ans[i][j] = row[i] + column[j] - a[i][j]
    
    for i in range(h):
        print(*ans[i])


if __name__ == "__main__":
    main()

