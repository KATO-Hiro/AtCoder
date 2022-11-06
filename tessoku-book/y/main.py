# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())

    c = [input().rstrip() for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1

    for i in range(h):
        for j in range(w):
            if c[i][j] == "#":
                continue

            if i + 1 < h:
                dp[i + 1][j] += dp[i][j]
            
            if j + 1 < w:
                dp[i][j + 1] += dp[i][j]
    
    print(dp[h - 1][w - 1])


if __name__ == "__main__":
    main()
