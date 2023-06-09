# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0, 0] + list(map(int, input().split()))
    dp = [0] * n
    dp[1] = a[1]
    memo = [-1] * n
    memo[1] = 0

    for i in range(2, n):
        tmp1 = dp[i - 1] + a[i]
        tmp2 = dp[i - 2] + b[i]

        if tmp1 <= tmp2:
            memo[i] = i - 1
            dp[i] = tmp1
        else:
            memo[i] = i - 2
            dp[i] = tmp2

    pos = n - 1
    ans = list()

    while pos != -1:
        ans.append(pos + 1)
        pos = memo[pos]

    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
