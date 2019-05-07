# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    diff = [0 for _ in range(n)]

    for i in range(1, n):
        if a[i] - a[i - 1] <= 0:
            diff[i] = 1

    d = list(accumulate(diff))
    ans = 0

    for j in range(n - k + 1):
        if d[j + k - 1] - d[j] == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
