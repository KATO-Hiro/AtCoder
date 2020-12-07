# -*- coding: utf-8 -*-


def main():
    from math import gcd

    n = int(input())
    ans = 1

    for i in range(2, n + 1):
        ans = ans * i // gcd(ans, i)

    print(ans + 1)


if __name__ == "__main__":
    main()
