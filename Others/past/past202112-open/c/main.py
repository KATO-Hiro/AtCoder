# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)

    for i in range(n):
        pi, vi = input().split()

        if vi == "AC" and pi not in d.keys():
            d[pi] = i + 1
    
    for key in sorted(d.keys()):
        print(d[key])


if __name__ == "__main__":
    main()
