# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, m = map(int, input().split())
    imos = [0 for _ in range(n + 1)]

    for i in range(m):
        li, ri = map(int, input().split())
        imos[li - 1] += 1
        imos[ri] += -1

    count = 0

    for i in list(accumulate(imos)):
        if i >= m:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
