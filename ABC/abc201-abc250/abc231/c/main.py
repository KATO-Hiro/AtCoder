# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline
    
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    for i in range(q):
        xi = int(input())

        index = bisect_left(a, xi)
        print(n - index)


if __name__ == "__main__":
    main()
