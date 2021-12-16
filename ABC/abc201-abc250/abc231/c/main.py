# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_right
    import sys

    input = sys.stdin.readline
    
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    for i in range(q):
        xi = int(input())
        xi -= 1

        index = bisect_right(a, xi)
        print(n - index)


if __name__ == "__main__":
    main()
