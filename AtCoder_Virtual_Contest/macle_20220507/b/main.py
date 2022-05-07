# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    dp = [1] * 2

    for i in range(n):
        ndp = [0] * 2

        for y in range(2):
            for x in range(2):
                if s[i] == "AND":
                    ndp[y & x] += dp[y]
                else:
                    ndp[y | x] += dp[y]

        dp = ndp
    
    print(dp[1])


if __name__ == "__main__":
    main()
