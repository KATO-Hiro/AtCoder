# -*- coding: utf-8 -*-


def main():
    from math import ceil

    x = int(input())
    ans = ceil(2 * x / 11)

    if x % 11 == 6:
        ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
