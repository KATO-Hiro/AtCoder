# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    base = 0

    for value in c.values():
        base += value * (value - 1) // 2
    
    for ai in a:
        tmp = base
        tmp -= c[ai] * (c[ai] - 1) // 2 
        tmp += (max(0, c[ai] - 1)) * (max(0, c[ai] - 2)) // 2 
        print(tmp)


if __name__ == "__main__":
    main()
