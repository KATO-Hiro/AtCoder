# -*- coding: utf-8 -*-


def solve():
    n = int(input())
    p = list(map(int, input().split()))

    def rec(left, right):
        if right - left == 1:
            return

        mid = (left + right) // 2
        left_min = min(p[left:mid])
        right_min = min(p[mid:right])

        if left_min > right_min:
            p[left:mid], p[mid:right] = p[mid:right], p[left:mid]

        rec(left, mid)
        rec(mid, right)

    rec(0, 1 << n)
    print(*p)


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
