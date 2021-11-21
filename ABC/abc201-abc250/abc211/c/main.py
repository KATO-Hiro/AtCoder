# -*- coding: utf-8 -*-



def main():
    s = input()
    n = len(s)
    dp = [[0 for _ in range(9)] for _ in range(10 ** 5 + 10)]
    dp[0][0] = 1
    mod = 10 ** 9 + 7

    for i in range(n):
        for j in range(9):
            dp[i + 1][j] += dp[i][j]

            if s[i] == 'c' and j == 0: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'h' and j == 1: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'o' and j == 2: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'k' and j == 3: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'u' and j == 4: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'd' and j == 5: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'a' and j == 6: 
                dp[i + 1][j + 1] += dp[i][j]
            if s[i] == 'i' and j == 7: 
                dp[i + 1][j + 1] += dp[i][j]
        
        for j in range(9):
            dp[i + 1][j] %= mod

    print(dp[n][8])


if __name__ == "__main__":
    main()
