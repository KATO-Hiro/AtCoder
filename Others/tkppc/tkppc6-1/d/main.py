# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(list(accumulate([0] + a)))
    mod = 998244353
    ans = 0

    for i in range(n + 1):
        ans += (2 * i - n) * b[i]
        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()
