# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    mod = 998244353
    dp = defaultdict(int)
    dp[""] = 1

    for si in s:
        ndp = defaultdict(int)

        for pattern, count in dp.items():
            for nc in ["A", "B"]:
                if si != "?" and si != nc:
                    continue

                t = pattern + nc

                if len(t) >= k and t == t[::-1]:
                    continue

                nt = t

                if len(t) >= k:
                    nt = t[1:]

                ndp[nt] += count
                ndp[nt] %= mod

        dp = ndp

    ans = sum(dp.values()) % mod
    print(ans)


if __name__ == "__main__":
    main()
