# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline
    
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [tuple(map(int, input().split())) for _ in range(m)]
    d = defaultdict(int)

    for xi, yi in xy:
        d[xi] = yi

    for i, ai in enumerate(a, 2):
        if t - ai <= 0:
            print("No")
            exit()
        
        t -= ai
        t += d[i]
    
    print("Yes")


if __name__ == "__main__":
    main()
