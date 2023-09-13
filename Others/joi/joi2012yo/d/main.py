# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    given = defaultdict(int)

    for _ in range(k):
        ai, bi = map(int, input().split())
        given[ai] = bi

    # 直前の3日の情報を保持
    dp = defaultdict(int)
    dp["000"] = 1
    mod = 10**4
    ng = ["111", "222", "333"]

    for i in range(1, n + 1):
        ndp = defaultdict(int)
        kinds = range(1, 4)

        if given[i] != 0:
            kinds = [given[i]]

        for j in kinds:
            for key in dp.keys():
                next_key = "".join(list(key + str(j))[1:])

                if next_key in ng:
                    continue

                ndp[next_key] += dp[key]
                ndp[next_key] %= mod

        dp = ndp

    ans = 0

    for dp_i in dp.values():
        ans += dp_i
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
