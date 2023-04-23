# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))
    d = defaultdict(list)
    c1 = 0

    for i, (ci, ri) in enumerate(zip(c, r), 1):
        if i == 1:
            c1 = ci

        if ci not in d.keys():
            d[ci] = [(ri, i)]
        else:
            d[ci].append((ri, i))
    
    if t in d.keys():
        s = d[t]
        s = sorted(s, reverse=True)
        print(list(s)[0][1])
    else:
        s = d[c1]
        s = sorted(s, reverse=True)
        print(list(s)[0][1])
    

if __name__ == "__main__":
    main()
