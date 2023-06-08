# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    inf = 10**9
    dp = [inf] * (n + 1)
    dp[1] = 0
    prev_pos = [-1] * (n + 1)

    # DP + 復元
    for i in range(1, n + 1):
        hi = h[i - 1]

        prev_i1, prev_i2 = i - 1, i - 2

        if prev_i1 >= 0 and dp[i] > (dp[prev_i1] + abs(hi - h[prev_i1 - 1])):
            dp[i] = dp[prev_i1] + abs(hi - h[prev_i1 - 1])
            prev_pos[i] = prev_i1
        if prev_i2 >= 0 and dp[i] > (dp[prev_i2] + abs(hi - h[prev_i2 - 1])):
            dp[i] = dp[prev_i2] + abs(hi - h[prev_i2 - 1])
            prev_pos[i] = prev_i2

    ans = [n]
    pos = n

    while pos != -1:
        p = prev_pos[pos]
        pos = p

        if p != -1:
            ans.append(p)

    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
