# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (n + 1)

    for i in range(n + 1):
        ok = False

        for ai in a:
            if i >= ai and not dp[i - ai]:
                ok = True

        if ok:
            dp[i] = True

    if dp[n]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
