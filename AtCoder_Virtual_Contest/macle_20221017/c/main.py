# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(accumulate(range(n + 1)))
    mod = 10 ** 9 + 7
    ans = 1

    for i in range(k, n + 1):
        value_min = a[i - 1]
        value_max = a[n] - a[n - i]
        ans += value_max - value_min + 1
        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()
