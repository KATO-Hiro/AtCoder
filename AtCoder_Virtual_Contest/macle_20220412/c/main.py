# -*- coding: utf-8 -*-


def main():
    import sys

    from itertools import accumulate
    input = sys.stdin.readline

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = [i for i in range(n + 1)]
    b = list(accumulate(a))
    mod = 10 ** 9 + 7
    ans = 0

    for i in range(k, n + 2):
        value_max = b[n] - b[n - i]
        value_min = b[i - 1]

        if i == n + 1:
            ans += 1
        else:
            ans += value_max - value_min + 1

        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()
