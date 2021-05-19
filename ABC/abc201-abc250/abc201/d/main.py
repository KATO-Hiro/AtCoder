# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j, aij in enumerate(list(input().rstrip())):
            if aij == "+":
                a[i][j] = 1
            else:
                a[i][j] = -1

    dp = [[-(1 << 30) for _ in range(w)] for _ in range(h)]
    dp[h - 1][w - 1] = 0

    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if i + 1 < h:
                dp[i][j] = max(dp[i][j], a[i + 1][j] - dp[i + 1][j])
            if j + 1 < w:
                dp[i][j] = max(dp[i][j], a[i][j + 1] - dp[i][j + 1])

    score = dp[0][0]

    if score > 0:
        print("Takahashi")
    elif score < 0:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
