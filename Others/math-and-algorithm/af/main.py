# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for i in range(n)]
    ans = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            xi, yi = xy[i]
            xj, yj = xy[j]

            dist = sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
            ans = min(ans, dist)
    
    print(ans)


if __name__ == "__main__":
    main()
