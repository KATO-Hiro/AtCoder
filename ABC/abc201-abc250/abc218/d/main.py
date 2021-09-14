# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = dict()

    for i in range(n):
        xi, yi = map(int, input().split())

        if xi not in c.keys():
            c[xi]= [yi]
        else:
            c[xi].append(yi)
        
    d = Counter()
    
    for values in c.values():
        for v1, v2 in combinations(sorted(values), 2):
            d[(v1, v2)] += 1

    ans = 0

    for value in d.values():
        ans += value * (value - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
