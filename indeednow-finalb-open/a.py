# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    a = int(input())
    b = int(input())
    summed = [0] * (10 ** 6 + 1)
    mod = 10 ** 9 + 7

    for i in range(b + 1):
        summed[i] = ((i ** 2 * (i + 1)) // 2) % mod

    ans = list(accumulate(summed))
    print((ans[b] - ans[a - 1]) % mod)


if __name__ == '__main__':
    main()
