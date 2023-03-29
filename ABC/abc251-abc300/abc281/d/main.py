# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    size = 105
    # aiまででj個選んだときに、その総和 % dとしたときの総和の最大値
    dp = [[-1 for _ in range(size)] for _ in range(size)]
    dp[0][0] = 0

    for i in range(n):
        ndp = [[-1 for _ in range(size)] for _ in range(size)]

        for j in range(k + 1):
            for r in range(d):
                if (dp[j][r] == -1):
                    continue

                # aiを選ばない
                ndp[j][r] = max(ndp[j][r], dp[j][r])

                # aiを選ぶ
                nj = j + 1
                nr = (dp[j][r] + a[i]) % d
                ndp[nj][nr] = max(ndp[nj][nr], dp[j][r] + a[i])
        
        dp = ndp
    
    print(dp[k][0])
    

if __name__ == "__main__":
    main()
