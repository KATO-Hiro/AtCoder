# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    m = len(s)
    t = [input() for _ in range(n)] 

    dp = [0 for _ in range(m + 10)]
    dp[0] = 1
    mod = 10 ** 9 + 7

    for i in range(m + 1):
        for ti in t:
            ti_size = len(ti)
            v = i + ti_size

            if v > m:
                continue

            if s[i:v] == ti:
                dp[v] += dp[i]
                dp[v] %= mod
        
    print(dp[m] % mod)


if __name__ == "__main__":
    main()
