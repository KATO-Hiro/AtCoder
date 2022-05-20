# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    first = 1
    second = 1
    mod = 10 ** 9 + 7
    ans = 0

    for i in range(3, n + 1):
        ans = first + second
        ans %= mod

        first = second
        first %= mod
        second = ans
        second %= mod
    
    print(ans % mod)


if __name__ == "__main__":
    main()
