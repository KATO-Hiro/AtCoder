# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(5, -1, -1):
        if 10 ** (i + 3) <= n < 10 ** (i + 4):
            n //= 10 ** (i + 1)
            n *= 10 ** (i + 1)
            print(n)
            exit()

    print(n)


if __name__ == "__main__":
    main()
