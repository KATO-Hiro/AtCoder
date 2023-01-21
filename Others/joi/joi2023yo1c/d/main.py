# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    rank = 1

    for key, value in sorted(c.items()):
        c[key] = rank
        rank += value
    
    for ai in a:
        print(c[ai])
   

if __name__ == "__main__":
    main()
