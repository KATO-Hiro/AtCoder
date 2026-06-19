# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b, c = map(int, input().split())
    mod = 10**9 + 7
    m = a * b * c
    ans = 1

    for _ in range(n):
        ans *= m
        ans %= mod
        m -= 1

    print(ans)


if __name__ == "__main__":
    main()
