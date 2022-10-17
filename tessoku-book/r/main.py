# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (s + 1)
    dp[0] = True

    # See:
    # https://atcoder.jp/contests/tessoku-book/submissions/34883889

    for ai in a:
        # 逆から回す
        for i in range(s, 0, -1):
            if i - ai < 0:
                break

            # 遷移がシンプルに書ける
            dp[i] |= dp[i - ai]
    
    if dp[s]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
