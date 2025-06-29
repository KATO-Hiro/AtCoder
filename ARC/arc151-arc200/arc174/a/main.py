# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10**18
    # 1倍、C倍、1倍の区間
    dp = [-inf] * 3
    dp[0] = 0

    for ai in a:
        ndp = [-inf] * 3

        for i in range(3):
            if dp[i] == -inf:
                continue

            for j in range(i, 3):
                if j != 1:
                    ndp[j] = max(ndp[j], dp[i] + ai)
                else:
                    ndp[j] = max(ndp[j], dp[i] + ai * c)

        dp = ndp

    ans = max(dp)
    print(ans)


if __name__ == "__main__":
    main()
