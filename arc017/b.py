# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    is_decreased = [0 for _ in range(n)]
    ans = 0

    for j in range(1, n):
        if a[j] <= a[j - 1]:
            is_decreased[j] = 1

    summed = list(accumulate([0] + is_decreased))

    for i in range(n - k + 1):
        diff = summed[i + k] - summed[i + 1]

        if diff == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
