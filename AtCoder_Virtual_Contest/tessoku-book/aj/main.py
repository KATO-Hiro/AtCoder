# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    n_min = 2 * (n - 1)

    if n_min > k:
        print("No")
        exit()

    if (k - n_min) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
