# -*- coding: utf-8 -*-


def main():
    from bisect import bisect, bisect_right
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    ans = 0

    for bi in b:
        i = bisect_right(a, bi - 1)
        j = bisect(c, bi)
        ans += i * (n - j)
    
    print(ans)


if __name__ == "__main__":
    main()
