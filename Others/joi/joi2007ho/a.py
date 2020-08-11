# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    summed = list(accumulate([0] + a))
    ans = 0

    for i in range(n - k + 1):
        ans = max(ans, summed[i + k] - summed[i])

    print(ans)


if __name__ == '__main__':
    main()
