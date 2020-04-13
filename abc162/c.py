# -*- coding: utf-8 -*-


def main():
    from math import gcd

    k = int(input())
    ans = 0

    for a in range(1, k + 1):
        for b in range(1, k + 1):
            for c in range(1, k + 1):
                tmp = gcd(a, b)
                ans += gcd(tmp, c)

    print(ans)


if __name__ == '__main__':
    main()
