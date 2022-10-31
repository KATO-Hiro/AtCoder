# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for i, ai in enumerate(a):
        j = bisect(a, ai - k - 1)
        ans += i - j

    print(ans)


if __name__ == "__main__":
    main()
