# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 9 + 7
    m = n * (n + 1) // 2
    print(m ** 2 % mod)


if __name__ == "__main__":
    main()
