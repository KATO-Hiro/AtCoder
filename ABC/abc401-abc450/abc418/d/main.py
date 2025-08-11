# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = input().rstrip()

    dp = [0] * 2
    ans = 0

    for i in range(1, n + 1):
        ndp = [0] * 2

        if t[i - 1] == "0":
            ndp[0] = dp[1]
            ndp[1] = dp[0] + 1
        else:
            ndp[0] = dp[0] + 1
            ndp[1] = dp[1]

        ans += ndp[0]
        dp = ndp

    print(ans)


if __name__ == "__main__":
    main()
