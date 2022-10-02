# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (n + 1) for _ in range(s + 1)]
    dp[0][0] = True

    for j in range(n):
        for i in range(s + 1):
            ai, bi = ab[j]

            if ai + i <= s and dp[i][j]:
                dp[ai + i][j + 1] = True
            if bi + i <= s and dp[i][j]:
                dp[bi + i][j + 1] = True
    
    if dp[s][n] > 0:
        print("Yes")
        
        ans = ""
        pos = s

        for i in reversed(range(1, n + 1)):
            ai, bi = ab[i - 1]

            if pos >= ai and dp[pos - ai][i - 1]:
                ans += "H"
                pos -= ai
            elif pos >= bi and dp[pos - bi][i - 1]: 
                ans += "T"
                pos -= bi
        
        print(ans[::-1])
    else:
        print("No")


if __name__ == "__main__":
    main()
