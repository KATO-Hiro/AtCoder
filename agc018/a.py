# -*- coding: utf-8 -*-


def main():
    from fractions import gcd

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_gcd = a[0]

    for i in range(n - 1):
        max_gcd = min(max_gcd, gcd(a[i], a[i + 1]))

    if k <= max_a and k % max_gcd == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
