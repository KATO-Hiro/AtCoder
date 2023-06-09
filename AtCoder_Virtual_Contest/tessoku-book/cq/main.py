# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[False for _ in range(n + 1)] for _ in range(s + 1)]
    dp[0][0] = True

    for j, aj in enumerate(a):
        for i in range(s + 1):
            if not dp[i][j]:
                continue

            dp[i][j + 1] = True

            if i + aj <= s:
                dp[i + aj][j + 1] = True

    if dp[s][n]:
        j = s
        ans = list()

        for i in range(n, 0, -1):
            tmp = j - a[i - 1]

            if tmp >= 0 and dp[tmp][i - 1]:
                ans.append(i)
                j = tmp

        print(len(ans))
        print(*ans[::-1])
    else:
        print(-1)


if __name__ == "__main__":
    main()
