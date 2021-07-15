# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = sum([abs(ai - bi) for ai, bi in zip(a, b)])

    if diff > k:
        print("No")
        exit()

    if (k - diff) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
