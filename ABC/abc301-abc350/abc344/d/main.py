# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = input().rstrip()
    m = len(t)
    n = int(input())
    dp = {"": 0}
    inf = 10**9

    for _ in range(n):
        ndp = dp.copy()
        __, *si = list(map(str, input().rstrip().split()))

        for u, cost in dp.items():
            for sij in si:
                nu = u + sij

                if not t.startswith(nu):
                    continue

                ndp[nu] = min(ndp.get(nu, inf), cost + 1)

        dp = ndp

    ans = dp.get(t, -1)
    print(ans)


if __name__ == "__main__":
    main()
