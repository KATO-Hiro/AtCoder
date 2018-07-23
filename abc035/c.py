# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def main():
    from itertools import accumulate

    n, q = list(map(int, input().split()))
    pieces = [0 for _ in range(n + 1)]

    for i in range(q):
        l, r = list(map(int, input().split()))
        pieces[l - 1] += 1
        pieces[r] -= 1

    imos = list(accumulate(pieces))
    result = ''

    for i in range(len(imos) - 1):
        if imos[i] % 2 == 0:
            result += '0'
        else:
            result += '1'

    print(result)


if __name__ == '__main__':
    main()
