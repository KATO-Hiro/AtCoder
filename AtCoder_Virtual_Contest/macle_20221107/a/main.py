# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)
    
    for i in range(n):
        _, *a = list(map(int, input().split()))
        d[tuple(a)] += 1
    
    print(len(d.keys()))


if __name__ == "__main__":
    main()
