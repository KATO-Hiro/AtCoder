# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = 1
    b = 1
    mod = 10 ** 9 + 7

    for i in range(3, n + 1):
        a, b = b, a + b
        b %= mod
    
    print(b)


if __name__ == "__main__":
    main()
