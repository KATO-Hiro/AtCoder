# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    inf = 10 ** 10
    a = [0] + sorted(list(map(int, input().split()))) + [inf]
    b = list(accumulate(a))
    x = [int(input()) for _ in range(q)]

    for xi in x:
        index = bisect(a, xi)
        index -= 1
        ans = (index * xi) - b[index]
        ans += (b[n] - b[index]) - ((n - index) * xi)
        print(ans)


if __name__ == "__main__":
    main()
