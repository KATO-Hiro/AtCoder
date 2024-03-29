# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    d = defaultdict(int)

    for ci, pi in zip(c, p):
        if ci not in d.keys():
            d[ci] = pi
        else:
            d[ci] = min(d[ci], pi)
    
    if len(d.keys()) < k:
        print(-1)
    else:
        sorted_d = sorted(d.values())
        print(sum(sorted_d[:k]))


if __name__ == "__main__":
    main()
