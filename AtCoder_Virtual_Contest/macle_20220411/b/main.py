# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]

    for ai in a[1:]:
        g = gcd(g, ai)
    
    print(g)


if __name__ == "__main__":
    main()
