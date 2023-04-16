# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    q = int(input())
    d1 = defaultdict(list)
    d2 = defaultdict(set)

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            i, j = qi[1], qi[2]
            d1[j].append(i)
            d2[i].add(j)
        elif qi[0] == 2:
            print(*sorted(d1[qi[1]]))
        else:
            print(*(sorted(d2[qi[1]])))
    

if __name__ == "__main__":
    main()
