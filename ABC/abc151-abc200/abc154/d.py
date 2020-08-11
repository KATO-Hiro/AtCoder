# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = map(int, input().split())
    p = [int(i) + 1 for i in input().split()]
    e = list(accumulate([0] + p))
    ans = 0

    for j in range(n - k + 1):
        ans = max(ans, e[j + k] - e[j])

    print(ans / 2)


if __name__ == '__main__':
    main()
