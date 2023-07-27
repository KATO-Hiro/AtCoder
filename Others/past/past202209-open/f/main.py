# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for i in range(n):
        ci = int(input())

        if ci >= 1:
            xi = list(map(int, input().split()))

            for xij in xi:
                d[xij].append(i + 1)

    # print(d)
    q = int(input())

    for j in range(q):
        dj = int(input())
        candidates = set([i for i in range(1, n + 1)])

        if dj == 0:
            _ = input().rstrip()
        else:
            yj = list(map(int, input().split()))

            # TLEになるのでは?
            for yjk in yj:
                for djk in d[yjk]:
                    if djk in candidates:
                        candidates.remove(djk)

        value = 0
        ans = -1

        for i, ai in enumerate(a, 1):
            if i in candidates:
                if ai > value:
                    value = ai
                    ans = i
        # print(candidates)

        print(ans)


if __name__ == "__main__":
    main()
