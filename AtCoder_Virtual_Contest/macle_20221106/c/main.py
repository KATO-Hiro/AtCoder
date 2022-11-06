# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    value_max = 10 ** 6 + 1
    c = [0] * value_max
    is_pairwise = True

    for ai in a:
        c[ai] += 1

    for i in range(2, value_max):
        count = 0
        
        for j in range(i, value_max, i):
            count += c[j]
        
        if count > 1:
            is_pairwise = False
            break
    
    g = 0

    for ai in a:
        g = gcd(ai, g)

    if is_pairwise:
        print("pairwise coprime")
    elif g == 1:
        print("setwise coprime")
    else:
        print("not coprime")


if __name__ == "__main__":
    main()
