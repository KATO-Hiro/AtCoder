# -*- coding: utf-8 -*-


def solve():
    n, a, b = map(int, input().split())
    c = n - a

    if (a > n) or (c**2 < b) or ((c + 1) // 2 * c < b):
        print("No")
    else:
        print("Yes")


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
