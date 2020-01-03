# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    dp = [[0 for _ in range(n + 1)] for _ in range(3)]

    for index, ti in enumerate(t, 1):
        if index <= k:
            if ti == 'r':
                dp[2][index] = p
            elif ti == 's':
                dp[0][index] = r
            elif ti == 'p':
                dp[1][index] = s
        else:
            if ti == 'r' and dp[2][index - k] == 0:
                dp[2][index] = p
            elif ti == 's' and dp[0][index - k] == 0:
                dp[0][index] = r
            elif ti == 'p' and dp[1][index - k] == 0:
                dp[1][index] = s

    ans = 0

    for d in dp:
        ans += sum(d)

    print(ans)


if __name__ == '__main__':
    main()
