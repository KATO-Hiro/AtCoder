# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (s + 1)
    dp[0] = 1

    for j in range(n):
        ndp = [0] * (s + 1)

        for i in range(s + 1):
            ndp[i] += dp[i]

            if i + a[j] <= s:
                ndp[i + a[j]] += dp[i]

        dp = ndp
    
    if dp[s] >= 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
