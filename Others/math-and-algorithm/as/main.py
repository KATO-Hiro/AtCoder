# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 9 + 7
    ans = (pow(4, n + 1, mod) - 1)
    ans *= pow((4 - 1), mod - 2, mod) 
    ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
