# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    _ = int(input())
    a = [-10 ** 10] + sorted(set(map(int, input().split()))) + [10 ** 10]
    q = int(input())

    for _ in range(q):
        bi = int(input())

        index = bisect_left(a, bi)
        ans = min(abs(a[index] - bi), abs(a[index - 1] - bi))

        print(ans)


if __name__ == "__main__":
    main()
