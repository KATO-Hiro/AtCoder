# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    c = Counter()

    for ti in t:
        c[ti] += 1
    
    for si in s:
        if si in c.keys():
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
