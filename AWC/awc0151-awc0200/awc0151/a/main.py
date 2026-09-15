# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = [int(input()) for _ in range(m)]

    if n * k >= sum(a):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
