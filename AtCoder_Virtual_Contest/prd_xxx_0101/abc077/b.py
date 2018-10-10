# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n = int(input())
    ans = 0

    for i in range(int(sqrt(n)) + 1):
        ans = max(ans, i ** 2)

    print(ans)


if __name__ == '__main__':
    main()
