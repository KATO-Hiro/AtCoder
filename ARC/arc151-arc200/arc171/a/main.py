# -*- coding: utf-8 -*-


def solve():
    n, a, b = map(int, input().split())
    c = min(n - a, (n + 1) // 2)

    if a > n:
        print("No")
    elif (n - a) * c >= b:
        print("Yes")
    else:
        print("No")


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
