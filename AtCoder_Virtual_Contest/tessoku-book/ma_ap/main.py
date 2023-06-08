# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x, y = 1, 1
    mod = 10**9 + 7

    for i in range(3, n + 1):
        z = x + y
        z %= mod
        x, y = y, z

        x %= mod
        y %= mod

        if i == n:
            print(z)
            exit()


if __name__ == "__main__":
    main()
