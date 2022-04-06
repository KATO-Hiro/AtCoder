# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]

    for ai in a:
        ans = gcd(ans, ai)
    
    print(ans)


if __name__ == "__main__":
    main()
