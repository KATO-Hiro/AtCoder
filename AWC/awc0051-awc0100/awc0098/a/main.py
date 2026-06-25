# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    t = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        ti = t[i]
        ai = a[i]
        s = sum([abs(aij - ti) for aij in ai])
        ans = max(ans, s)

    print(ans)


if __name__ == "__main__":
    main()
