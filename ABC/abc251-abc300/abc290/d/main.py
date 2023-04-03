# -*- coding: utf-8 -*-


def solve():
    from math import gcd

    n, d, k = map(int, input().split())
    k -= 1
    g = gcd(n, d)
    ans = (k * d) % n +  k // (n // g)
    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()
    

if __name__ == "__main__":
    main()
