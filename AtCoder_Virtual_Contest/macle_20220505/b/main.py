# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left, bisect_right
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 0

    for ai in a:
        index1 = bisect_left(a, ai - 1)
        index2 = bisect_right(a, ai + 1)
        size = index2 - index1
        ans = max(ans, size)
    
    print(ans)


if __name__ == "__main__":
    main()
