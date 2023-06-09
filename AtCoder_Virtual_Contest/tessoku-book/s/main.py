# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    dp = [0] * (w + 1)

    for _ in range(n):
        wi, vi = map(int, input().split())

        # 遷移を逆にすると、シンプルに書ける
        for j in range(w, wi - 1, -1):
            dp[j] = max(dp[j], dp[j - wi] + vi)

    print(max(dp))


if __name__ == "__main__":
    main()
