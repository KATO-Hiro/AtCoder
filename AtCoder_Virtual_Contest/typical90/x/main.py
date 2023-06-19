# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = 0

    for ai, bi in zip(a, b):
        diff += abs(ai - bi)

    if k - diff >= 0 and (k - diff) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
