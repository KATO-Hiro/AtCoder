# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    ans = float("inf")

    for bi in b:
        index = bisect_left(a, bi)

        if index == n:
            index -= 1

        for j in range(max(0, index - 3), min(index + 3, n)):
            ans = min(ans, abs(a[j] - bi))

    print(ans)


if __name__ == "__main__":
    main()
