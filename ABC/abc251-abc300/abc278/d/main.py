# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    d = defaultdict(int)
    all = 0

    for i, ai in enumerate(a, 1):
        d[i] = ai

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            d = defaultdict(int)
            all = qi[1]
        elif qi[0] == 2:
            d[qi[1]] += qi[2]
        else:
            print(all + d[qi[1]])
    

if __name__ == "__main__":
    main()
