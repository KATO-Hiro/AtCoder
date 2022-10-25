# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    dp = [0] * (w + 1)

    for i in range(n):
        wi, vi = map(int, input().split())

        for j in range(w, wi - 1, -1):
            dp[j] = max(dp[j], dp[j - wi] + vi)

    print(dp[w])


if __name__ == "__main__":
    main()
