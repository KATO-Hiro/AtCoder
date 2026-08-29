# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, p = map(int, input().split())
    ans = 0

    for _ in range(n):
        di, vi = map(int, input().split())

        if di > m:
            continue

        ans += vi

    ans *= 100 - p
    ans //= 100

    print(ans)


if __name__ == "__main__":
    main()
