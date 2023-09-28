# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    x = int(input())
    size = 10**5 + 100
    dp = [False] * size
    dp[0] = True

    for i in range(x):
        for aj in a:
            if not dp[i]:
                continue

            ni = i + aj

            if ni > x:
                continue
            if ni in b:
                continue

            dp[ni] = True

    if dp[x]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
