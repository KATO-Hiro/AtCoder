# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = list()

    for i in range(n):
        xi, yi = map(int, input().split())
        xy.append((xi, yi))
    
    ans = 0
    
    for (x1, y1), (x2, y2), (x3, y3) in combinations(xy, 3):
        s = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2
    
        if s > 0:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
