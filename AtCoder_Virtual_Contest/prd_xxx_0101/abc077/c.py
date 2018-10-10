# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    from bisect import bisect_right

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    ans = 0

    for bi in b:
        less = bisect_left(a, bi)
        greater = n - bisect_right(c, bi)
        ans += less * greater

    print(ans)


if __name__ == '__main__':
    main()
