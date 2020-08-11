# -*- coding: utf-8 -*-


def main():
    from math import ceil
    n = int(input())
    ans = ''

    if n == 0:
        print(0)
        exit()

    while n != 0:
        mod_n = ceil(n / (-2))
        ans += str(n - mod_n * (-2))
        n = mod_n

    print(ans[::-1])


if __name__ == '__main__':
    main()
