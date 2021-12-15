# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a, b = [0] * n, [0] * n
    dp = [[False] * (s + 10) for _ in range(n + 10)]
    dp[0][0] = True

    for i in range(n):
        a[i], b[i] = map(int, input().split())
    
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            diff1 = j - a[i - 1]
            diff2 = j - b[i - 1]

            if diff1 >= 0 and dp[i - 1][diff1]:
                dp[i][j] = True

            if diff2 >= 0 and dp[i - 1][diff2]:
                dp[i][j] = True
    
    if dp[n][s]:
        ans = ""
        pos = s
        
        for i in range(n, 0, -1):
            ai = a[i - 1]
            bi = b[i - 1]

            if pos >= ai and dp[i - 1][pos - ai]:
                ans += "A"
                pos -= ai
            elif pos >= bi and dp[i - 1][pos - bi]: 
                ans += "B"
                pos -= bi

        print(ans[::-1])
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
