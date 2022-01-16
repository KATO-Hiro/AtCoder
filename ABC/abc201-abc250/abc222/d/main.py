# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    value_max = 3005
    dp = [0 for _ in range(value_max)]
    dp[0] = 1 # 初期化
    mod = 998244353
    
    for i in range(n):
        p = [0 for _ in range(value_max)]
        dp, p = p, dp
        p = list(accumulate(p))

        for j in range(3000 + 1):
            if a[i] <= j <= b[i]:
                dp[j] += p[j]
                dp[j] %= mod
        
    ans = 0

    for i in range(3000 + 1):
        ans += dp[i]
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
