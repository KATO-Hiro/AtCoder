# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    inf = 10**12
    d = defaultdict(lambda: inf)

    n = int(input())

    for _ in range(n):
        ai, ci = map(int, input().split())
        d[ci] = min(d[ci], ai)

    print(max(d.values()))


if __name__ == "__main__":
    main()
