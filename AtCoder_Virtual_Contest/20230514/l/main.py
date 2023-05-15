# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    dp = [False] * (x + 1)
    dp[0] = True

    for _ in range(n):
        ai, bi = map(int, input().split())

        for _ in range(bi):
            ndp = [False] * (x + 1)

            for xi in range(x + 1):
                if not dp[xi]:
                    continue

                # 選ばない
                ndp[xi] = dp[xi]

                # 選ぶ
                if (xi + ai) <= x:
                    ndp[xi + ai] = dp[xi]

            dp = ndp

    if dp[x]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
