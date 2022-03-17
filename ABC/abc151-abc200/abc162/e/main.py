# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    d = [0] * (k + 1)
    ans = 0
    
    for i in range(1, k + 1):
        d[i] = pow(k // i, n, mod)
    
    for i in range(k, 0, -1):
        for j in range(2 * i, k + 1, i):
            d[i] -= d[j]
            d[i] %= mod
    
    for i in range(1, k + 1):
        ans += d[i] * i
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
