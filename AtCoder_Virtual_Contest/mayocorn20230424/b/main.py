# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = [0] + list(accumulate(a))
    mod = 10 ** 9 + 7
    ans = 0

    for i in range(1, n):
        ans += a[i - 1] * (b[n] - b[i])
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
