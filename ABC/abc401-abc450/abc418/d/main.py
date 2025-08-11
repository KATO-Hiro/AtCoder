# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = input().rstrip()

    dp = [0] * 2
    ans = 0

    for ti in t:
        if ti == "0":
            dp[0], dp[1] = dp[1], dp[0]

        dp[int(ti)] += 1
        ans += dp[1]

    print(ans)


if __name__ == "__main__":
    main()
