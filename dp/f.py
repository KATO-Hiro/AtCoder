# -*- coding: utf-8 -*-


def main():
    s = list(input())
    n = len(s)
    t = list(input())
    m = len(t)
    # LCSの長さを状態として持つ
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # See:
    # https://qiita.com/drken/items/03c7db44ccd27820ea0d
    # LCSの求め方は蟻本のpp.56-57も参照
    # △文字列s, tを二次元配列の形で扱う
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    ans = ''
    i = n
    j = m

    # △復元
    # dp tableの値を見てどこから更新されたかを特定
    while i > 0 and j > 0:
        # (i - 1, j) -> (i, j)
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        # (i, j - 1) -> (i, j)
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        # (i - 1, j - 1) -> (i, j)
        else:
            ans = s[i - 1] + ans
            i -= 1
            j -= 1

    print(ans)


if __name__ == '__main__':
    main()
