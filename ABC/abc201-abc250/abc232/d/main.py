# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]
    dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if c[i][j] == "#":
                continue

            dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]) + 1
    
    print(dp[0][0])


if __name__ == "__main__":
    main()
