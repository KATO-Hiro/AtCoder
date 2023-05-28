# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    s = input().rstrip()

    # See:
    # https://atcoder.jp/contests/abc303/submissions/41736372
    # tupleで初期化 & 上書き
    dp = (0, z)

    for si in s:
        # CapsLockを押したときのコストを加算
        dp = min(dp[0], dp[1] + z), min(dp[1], dp[0] + z)

        if si == "a":
            dp = dp[0] + x, dp[1] + y
        else:
            dp = dp[0] + y, dp[1] + x

    print(min(dp))


if __name__ == "__main__":
    main()
