# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(set(a))
    m = len(b)
    ans = [0] * n

    for ai in a:
        index = bisect(b, ai)
        ans[m - index] += 1
    
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
