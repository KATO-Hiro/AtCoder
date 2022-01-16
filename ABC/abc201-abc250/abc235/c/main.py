# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for index, ai in enumerate(a, 1):
        d[ai].append(index)
    
    for i in range(q):
        xi, ki = map(int, input().split())

        if ki <= len(d[xi]):
            print(d[xi][ki - 1])
        else:
            print(-1)


if __name__ == "__main__":
    main()
