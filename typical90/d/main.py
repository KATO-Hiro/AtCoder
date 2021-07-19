# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    c = [list(accumulate(ai))[-1] for ai in a]
    a_t = [[0 for _ in range(h)] for _ in range(w)]

    for i in range(h):
        for j in range(w):
            a_t[j][i] = a[i][j]

    d = [list(accumulate(ai))[-1] for ai in a_t]
    ans = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            ans[i][j] = c[i] + d[j] - a[i][j]
    
    for i in range(h):
        print(*ans[i])


if __name__ == "__main__":
    main()

