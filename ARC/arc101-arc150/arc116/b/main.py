# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    mod = 998244353
    summed = 0
    ans = 0

    for i in range(n - 1, -1, -1):
        summed *= 2
        summed %= mod

        if i + 1 != n:
            summed += a[i + 1]

        ans += a[i] * (summed + a[i])
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
