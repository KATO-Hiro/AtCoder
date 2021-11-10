# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = [tuple(map(int, input().split())) for _ in range(n)]
    ans = set()

    for i in range(n):
        for j in range(i + 1, n):
            xi = x[i]
            xj = x[j]

            dx = xj[0] - xi[0]
            dy = xj[1] - xi[1]

            g = gcd(dx, dy)
            ans.add((dx // g, dy // g))
            ans.add((-dx // g, -dy // g))
    
    print(len(ans))


if __name__ == "__main__":
    main()
