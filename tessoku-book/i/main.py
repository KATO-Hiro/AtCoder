# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    ans = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    
    for _ in range(n):
        ai, bi, ci, di = map(int, input().split())
        ai -= 1
        bi -= 1
        ans[ai][bi] += 1
        ans[ci][bi] -= 1
        ans[ai][di] -= 1
        ans[ci][di] += 1

    for i in range(h):
        for j in range(1, w):
            ans[i][j] += ans[i][j - 1]
    
    for j in range(w):
        for i in range(1, h):
            ans[i][j] += ans[i - 1][j]
    
    for i in range(h):
        print(*ans[i][:-1])


if __name__ == "__main__":
    main()
