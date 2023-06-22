# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    da, db, dc = defaultdict(int), defaultdict(int), defaultdict(int)

    for ai, bi, ci in zip(a, b, c):
        da[ai % 46] += 1
        db[bi % 46] += 1
        dc[ci % 46] += 1

    ans = 0

    for ka, va in da.items():
        for kb, vb in db.items():
            for kc, vc in dc.items():
                if (ka + kb + kc) % 46 == 0:
                    ans += va * vb * vc

    print(ans)


if __name__ == "__main__":
    main()
