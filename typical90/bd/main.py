# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a, b = [0] * n, [0] * n
    dp = [[False] * (n + 10) for _ in range(s + 10)]
    dp[0][0] = True

    for i in range(n):
        a[i], b[i] = map(int, input().split())
    
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            diff1 = j - a[i - 1]
            diff2 = j - b[i - 1]

            if diff1 >= 0 and dp[diff1][i - 1]:
                dp[j][i] = True

            if diff2 >= 0 and dp[diff2][i - 1]:
                dp[j][i] = True
    
    if dp[s][n]:
        ans = ""
        pos = s
        
        for i in reversed(range(1, n + 1)):
            ai = a[i - 1]
            bi = b[i - 1]

            if pos >= ai and dp[pos - ai][i - 1]:
                ans += "A"
                pos -= ai
            elif pos >= bi and dp[pos - bi][i - 1]: 
                ans += "B"
                pos -= bi

        print(ans[::-1])
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
