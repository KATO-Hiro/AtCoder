# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())) + [-10 ** 10, 10 ** 10]) # 番兵を置く
    b = sorted(list(map(int, input().split())))
    ans = float("inf")

    for bi in b:
        j = bisect_left(a, bi)
        ans = min(ans, abs(a[j] - bi), abs(a[j - 1] - bi))

    print(ans)


if __name__ == "__main__":
    main()
