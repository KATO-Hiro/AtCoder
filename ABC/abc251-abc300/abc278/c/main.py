# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    d = defaultdict(set)

    for _ in range(q):
        ti, ai, bi = map(int, input().split())

        if ti == 1:
            d[ai].add(bi)
        elif ti == 2:
            d[ai].discard(bi)
        else:
            if bi in d[ai] and ai in d[bi]:
                print("Yes")
            else:
                print("No")
    

if __name__ == "__main__":
    main()
