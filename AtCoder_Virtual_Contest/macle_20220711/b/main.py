# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    n -= k
    ans += ceil(n / (k - 1))

    print(ans)


if __name__ == "__main__":
    main()
