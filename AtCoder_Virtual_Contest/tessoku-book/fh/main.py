# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w = int(input())
    mod = 10**9 + 7
    ans = 12 * pow(7, w - 1, mod) % mod
    print(ans)


if __name__ == "__main__":
    main()
