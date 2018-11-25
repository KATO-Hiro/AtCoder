# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    x = sorted(list(map(int, input().split())))
    summed_x = list(accumulate([0] + x))
    ans = 0

    for i in range(1, n):
        ans += summed_x[n] - summed_x[i] - x[i - 1] * (n - i)

    print(ans)


if __name__ == '__main__':
    main()
