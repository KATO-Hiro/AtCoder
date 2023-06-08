# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (s + 1)
    dp[0] = True

    for j, aj in enumerate(a):
        ndp = [False] * (s + 1)

        for i in range(s + 1):
            if not dp[i]:
                continue

            ndp[i] = True

            if i + aj > s:
                continue

            ndp[i + aj] = True

        dp = ndp

    if dp[s]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
