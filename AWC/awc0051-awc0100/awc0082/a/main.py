# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for _ in range(m):
        si, pi, di = map(int, input().split())
        pi -= 1
        cost = a[pi]

        if si == 1:
            cost = max(0, a[pi] - k)

        ans += cost * di

    print(ans)


if __name__ == "__main__":
    main()
