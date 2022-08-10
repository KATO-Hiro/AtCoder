# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0

    # See:
    # https://atcoder.jp/contests/abc262/submissions/33664314
    for k in range(1, n + 1):
        # 余りを状態として持つことをどうしたら思いつけるか?
        dp = [[0] * k for _ in range(k + 1)]  # dp[i][j]: 数列からi個を選択したときに、その総和 % mod kがjとなる組合せ
        dp[0][0] = 1

        for ai in a:
            # aiが巨大な数字である場合への対処
            ai %= k

            # ループを逆向きなのは、重複して数えるのを回避するためか?
            for i in range(k - 1, -1, -1):
                for j in range(k):
                    dp[i + 1][(j + ai) % k] += dp[i][j]
                    dp[i + 1][(j + ai) % k] %= mod
        
        ans += dp[k][0]
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
