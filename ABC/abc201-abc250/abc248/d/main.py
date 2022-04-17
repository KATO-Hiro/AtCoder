# -*- coding: utf-8 -*-


def main():
    from bisect import bisect, bisect_right, bisect_left
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for index, ai in enumerate(a, 1):
        d[ai].append(index)
    
    for key in d.keys():
        d[key].append(0)
        d[key].append(10 ** 6)
        d[key].sort()
    
    q = int(input())

    for i in range(q):
        li, ri, xi = map(int, input().split())

        if xi not in d.keys():
            print(0)
        else:
            di = d[xi]
            index_left = bisect_left(di, li)
            index_right = bisect(di, ri)
            print(index_right - index_left)


if __name__ == "__main__":
    main()
