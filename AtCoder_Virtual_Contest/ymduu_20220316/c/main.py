# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline
    k = int(input())
    ans = 0

    for a in range(1, k + 1):
        for b in range(1, k + 1):
            g = gcd(a, b)

            for c in range(1, k + 1):
                ans += gcd(g, c)
    
    print(ans)


if __name__ == "__main__":
    main()
