# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    r = list(map(int, input().split()))
    a = r[:]

    for i in range(n - 1):
        ni = i + 1
        a[ni] = min(a[ni], a[i] + 1)

    for j in range(n - 1, 0, -1):
        nj = j - 1
        a[nj] = min(a[nj], a[j] + 1)

    ans = 0

    for ri, ai in zip(r, a):
        if ri == ai:
            continue

        ans += abs(ri - ai)

    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
