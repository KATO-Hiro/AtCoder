# -*- coding: utf-8 -*-


def main():
    n = int(input())
    mod = 10 ** 9 + 7
    ans = 0

    for i in range(n):
        ans += ((i + 1) ** 10 - i ** 10) * (n // (i + 1)) ** 10
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
