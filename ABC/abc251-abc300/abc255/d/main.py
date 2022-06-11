# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = [0] + list(accumulate(a))
    x = [int(input()) for _ in range(q)]

    for xi in x:
        index = bisect_left(a, xi)
        ans = (index * xi) - b[index]
        ans += (b[n] - b[index]) - ((n - index) * xi)
        print(ans)


if __name__ == "__main__":
    main()
