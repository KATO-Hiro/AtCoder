# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = list()
    ans = set()

    for _ in range(n):
        xi, yi = map(int, input().split())
        xy.append((xi, yi))
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            xi, yi = xy[i]
            xj, yj = xy[j]
            xk, yk = xi - xj, yi - yj
            g = gcd(xk, yk)

            if g != 0:
                xk //= g
                yk //= g
            
            ans.add((xk, yk))
    
    print(len(ans))


if __name__ == "__main__":
    main()
