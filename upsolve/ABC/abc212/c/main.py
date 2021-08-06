# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [-10 ** 10] + sorted(list(map(int, input().split()))) + [10 ** 10]
    b = sorted(list(map(int, input().split())))
    ans = float("inf")

    for bi in b:
        index = bisect_left(a, bi)
        ans = min(ans, abs(a[index] - bi), abs(a[index - 1] - bi))
    
    print(ans)


if __name__ == "__main__":
    main()
