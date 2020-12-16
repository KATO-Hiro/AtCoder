# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    n -= 1
    a = 1
    b = 1

    for i in range(n, n - 11, -1):
        a *= i

    for j in range(2, 11 + 1):
        b *= j

    print(a // b)


if __name__ == "__main__":
    main()
