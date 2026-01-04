# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a1, a2, b = a[0], a[1], a[2:]
    b.sort()
    k = n - 2

    inf = 10**18
    ans = inf

    for i in range(k):
        j = i + m - 1

        if j >= k:
            break

        bi, bj = b[i], b[j]
        cost = max(0, a1 - bi) + max(0, bj - a2)
        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
