# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [True] * 2

    for i in range(1, n):
        ndp = [True] * 2

        if (dp[0] and abs(a[i - 1] - a[i]) <= k) or (dp[1] and abs(b[i - 1] - a[i]) <= k):
            pass
        else:
            ndp[0] = False

        if (dp[0] and (abs(a[i - 1] - b[i]) <= k) or (dp[1] and abs(b[i - 1] - b[i]) <= k)):
            pass
        else:
            ndp[1] = False
        
        dp = ndp
    
    if True in dp:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()
