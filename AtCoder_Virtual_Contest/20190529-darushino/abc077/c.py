# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    ans = 0

    for bi in b:
        a_count = bisect(a, bi - 1)
        c_count = n - bisect(c, bi)
        ans += a_count * c_count

    print(ans)


if __name__ == '__main__':
    main()
