# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    summed_a = sum(a)

    if summed_a > k:
        print("No")
    else:
        if (k - summed_a) % 2 == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
