# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    s = input().rstrip()
    inf = 10**18
    dp = [inf] * 2
    dp[0] = 0

    for si in s:
        ndp = [inf] * 2
        a = si == "A"

        for c in range(2):
            for nc in range(2):
                cost = x if a == nc else y

                if nc != c:
                    cost += z

                ndp[nc] = min(ndp[nc], dp[c] + cost)

        dp = ndp

    print(min(dp))


if __name__ == "__main__":
    main()
