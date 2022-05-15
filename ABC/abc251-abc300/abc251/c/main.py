# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline
    n = int(input())
    d = defaultdict(tuple)

    for i in range(n):
        si, ti = map(str, input().split())

        if si not in d.keys():
            d[si] = (int(ti), -(i + 1))
    
    e = sorted(d.values(), reverse=True)
    print(-e[0][1])


if __name__ == "__main__":
    main()
