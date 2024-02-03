# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    upper = 10**6
    ans = 0
    inf = upper * 2

    for x in range(upper + 1):
        y = inf
        ok = True

        for ai, bi, qi in zip(a, b, q):
            remain = qi - ai * x

            if remain < 0:
                ok = False
                break

            if bi == 0:
                continue

            y = min(y, remain // bi)

        if ok:
            ans = max(ans, x + y)

    print(ans)


if __name__ == "__main__":
    main()
