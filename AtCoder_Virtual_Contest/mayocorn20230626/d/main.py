# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[False for _ in range(n + 1)] for _ in range(s + 1)]
    dp[0][0] = True

    for j in range(n):
        ai, bi = ab[j]

        for i in range(s + 1):
            if not dp[i][j]:
                continue

            if i + ai <= s:
                dp[i + ai][j + 1] = True
            if i + bi <= s:
                dp[i + bi][j + 1] = True

    if dp[s][n]:
        print("Yes")

        # DPの復元
        pos, k = s, n
        ans = list()

        while k > 0:
            ai, bi = ab[k - 1]

            if pos - ai >= 0 and dp[pos - ai][k - 1]:
                ans.append("H")
                pos -= ai
            elif pos - bi >= 0 and dp[pos - bi][k - 1]:
                ans.append("T")
                pos -= bi

            k -= 1

        print("".join(ans[::-1]))
    else:
        print("No")


if __name__ == "__main__":
    main()
