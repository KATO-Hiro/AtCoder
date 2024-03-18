# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = input().rstrip()
    m = len(t)
    n = int(input())
    t2 = "?" + t[::-1] + "?" * 110

    inf = 10**18
    dp = [inf] * 220
    dp[0] = 0
    s = [tuple(map(str, input().split())) for _ in range(n)][::-1]

    for _s in s:
        _, *si = _s
        ndp = dp[:]

        for sij in si:
            sij = sij[::-1]

            for start in range(1, m + 1):
                ok = True

                for k, sijk in enumerate(sij):
                    if t2[start + k] != sijk:
                        ok = False
                        break

                if ok:
                    size = len(sij)
                    ndp[start + size - 1] = min(
                        dp[start - 1] + 1, ndp[start + size - 1]
                    )

        dp = ndp

    ans = dp[m]

    if ans >= inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
