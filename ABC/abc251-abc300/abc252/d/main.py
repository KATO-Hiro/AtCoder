# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)

    # 整数の頻度分布に対して、j個選んだときの組み合わせを求める
    dp = [0] * 4
    dp[0] = 1

    for ci in c.values():
        ndp = [0] * 4

        for j in range(4):
            # c[i]を選ばない
            ndp[j] = dp[j]

            # c[i]を選ぶ
            if (j - 1) >= 0:
                ndp[j] += dp[j - 1] * ci
        
        dp = ndp
    
    print(dp[3])


if __name__ == "__main__":
    main()
