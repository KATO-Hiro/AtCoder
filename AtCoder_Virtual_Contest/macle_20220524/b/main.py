# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    mod = 10 ** 9 + 7

    if abs(n - m) >= 2:
        print(0)
        exit()

    p = list()
    value = 1

    for i in range(1, 10 ** 5 + 1):
        value *= i
        value %= mod
        p.append(value)
    
    ans = p[n - 1] * p[m - 1]

    if (n == m):
        ans *= 2

    ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()
