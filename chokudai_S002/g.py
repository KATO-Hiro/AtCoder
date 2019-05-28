# -*- coding: utf-8 -*-


def main():
    from fractions import gcd

    n = int(input())

    for i in range(n):
        ai, bi = map(int, input().split())
        print(gcd(ai, bi))


if __name__ == '__main__':
    main()
