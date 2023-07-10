# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = [i for i in range(n + 1)]
    b = list(accumulate(a))
    c = list(accumulate(a[::-1]))
    mod = 10**9 + 7
    ans = 0

    for i in range(k - 1, n + 1):
        value_max = c[i]
        value_min = b[i]
        ans += value_max - value_min + 1
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
