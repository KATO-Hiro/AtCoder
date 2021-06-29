# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = p - 1

    print(ans * pow(p - 2, n - 1, mod) % mod)


if __name__ == "__main__":
    main()
